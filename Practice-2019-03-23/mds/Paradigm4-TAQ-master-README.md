# Example SciDB queries for trade and quote data

You will need the following plugins to run all the examples here:

* accelerated_io_tools (https://github.com/paradigm4/accelerated_io_tools)
* axial_aggregate (contact Paradigm4)

## Obtain example data

The example queries here use the following example data obtained from Nyxdata:

```
wget ftp://ftp.nyxdata.com/Historical%20Data%20Samples/Daily%20TAQ/EQY_US_ALL_NBBO_20131218.zip
wget ftp://ftp.nyxdata.com/Historical%20Data%20Samples/Daily%20TAQ/EQY_US_ALL_TRADE_20131218.zip
```

The example data file format specification is available from:
`http://www.nyxdata.com/doc/224904`


## Loading the data into ScIDB

The trades_load.sh and trades_redim.sh scripts load the
EQY_US_ALL_TRADE_20131218.zip data and redimension them into a ms (time) by
symbol_index 2-d SciDB array. The script also creates an auxiliary mapping
array named 'tkr' between string ticker symbol and integer symbol index.

The quotes_load.sh and quotes_redim.sh script does the same thing but for the
EQY_US_ALL_NBBO quote data file.

Run the following to load and redimension the example data

```
./trades_load.sh
./trades_redim.sh

./quotes_load.sh
./quotes_redim.sh
```

## Looking up trades by symbol string

Join with the auxiliary `tkr` array to look up data by ticker symbol name.
Here are examples that count the number of trades and quotes for 'BAM'.

```
iquery -aq "
op_count(
  cross_join(trades as x, filter(tkr, symbol='BAM') as y, x.symbol_index, y.symbol_index)
)"

## {i} count
## {0} 6337

iquery -aq "
op_count(
  cross_join(quotes as x, filter(tkr, symbol='BAM') as y, x.symbol_index, y.symbol_index)
)"

## {i} count
## {0} 49667
```

As expected we see more quotes than trades for this instrument. Note that you can
also just filter directly by symbol index using `between` if you know it. For example:

```
iquery -aq "filter(tkr, symbol='BAM')"

## {symbol_index} symbol
## {615} 'BAM'


iquery -aq "
op_count(
   between(trades, null,615,0, null,615,null)
)"

## {i} count
## {0} 6337
```

## Computing minute bars

The trade data are now organized by symbol, time, and a dummy coordinate that
separates collisions (due to, say exchanges)  in a sparse array.

The following query computes and store one-minute open/high/low/close bars from
these data. We need some extra aggregates from the axial_aggregate plugin:
load that:
```
iquery -naq "load_library('axial_aggregate')"
iquery -naq "
store(
  slice(
    regrid(
      apply(
              trades, 
              timeprice, tuple(ms, price)
            ), 
            1000, 1, 60000,
            axial_first(timeprice) as open,
            max(price) as high,
            min(price) as low,
            axial_last(timeprice) as close
          ),
          dummy,0
        ),
  minute_bars
)"
```

This query runs in seconds, even on modest desktop machines. It
produces one-minute bars for _all_ stock trade data at once.

Let's deconstruct the query:

`apply(trades, timeprice, tuple(ms, price))` creates a tuple using the timestamp `ms` and the price `price` and stores the tuple into a new attribute `timeprice`. Storing data in tuple is required to calculate the open and close values within the minute bars (using `axial_first` and `axial_last` respectively)

`regrid(... , 1000, 1, 60000, ...)` applies the open/high/low/close summary
statistics over regular rectilinear regions along the coordinate axes.  The
rectangles have dimension 1000 (dummy) by 1 (symbol) by 60000 milliseconds.
That means we compute the open/high/low/close price over all sequence numbers
for each symbol per one minute.

`slice(..., dummy ,0)` removes the dummy sequence number coordinate axis from
 the result. It's no longer needed because all trades for each symbol and
 minute have been accounted for in the regrid aggregate. So slice simply
 removes this no longer used axis.

We're left with an array named 'minute_bars' that has two dimensions:
`symbol_index` and 60000 ms (that is, minutes). The array is still sparse
beause some thinly traded instruments may not have had any trades in some of
the minute intervals.


Let's pull out one of these minute bar time series for a particuar stock,
CVS.  We can consult the symbols array to find it's index directly.
```
iquery -aq "filter(apply(tkr,x,regex(symbol, 'CVS')), x=true)"
# {i} symbol,x
# {1612} 'CVS',true
```
So this says that symbol index 1612 corresponds to CVS.

We can  use SciDB's cross_join to avoid an explicit index lookup. We do need
to use a repart to bring the symbols array schema into a conformable chunking
scheme with the minute_bars array. Only the first 10 minutes of bars are
shown below:

```
iquery -aq "
cross_join(
  minute_bars as A,
    project(
      filter(apply(tkr,x,regex(symbol, 'CVS')), x=true),symbol) as B,
  A.symbol_index, B.symbol_index)" | head -n 10

# {symbol_index,ms} open,high,low,close,symbol
# {1612,513} 72,72,67.1,67.1,'CVS'
# {1612,560} 70.1,70.1,70.1,70.1,'CVS'
# {1612,561} 70.1,70.2,70.1,70.2,'CVS'
# {1612,563} 70.2,70.2,70.2,70.2,'CVS'
# {1612,565} 70.2,70.2,70.2,70.2,'CVS'
# {1612,568} 70.2,70.2,70.2,70.2,'CVS'
# {1612,569} 70.2,72.4,70.2,72.4,'CVS'
# {1612,570} 68.2,73.7,68.2,70,'CVS'
# {1612,571} 69.75,76.9,68,75.818,'CVS'
```
Note! That  570 minutes = 9:30 AM.



## Computing VWAP for all trades

Let's turn to another common kind of operation, computing volume-weighted
average price (VWAP). We'll compute it for every instrument across their raw
trade data in the array tades, and store the result into a new array called
'VWAP'.
```
iquery -naq "
store(
  apply(
    cumulate(
      apply(trades, pv, price*volume),
      sum(pv) as numerator,
      sum(volume) as denominator, ms),
    vwap, numerator/denominator),
  VWAP)"
```

This query runs pretty quickly even on modest hardware. It computes and stores
vwap on the millisecond data for all instruments. Here is a brief overview of
each step:

- `apply(trades, pv, price*volume)` adds a new attribute named 'pv' to the trades array that contains price*volume for every symbol and every time.
- `cumulate(..., sum(pv), sum(volume), ms)` computes the cumulative sum of the 'pv' and 'volume' attibutes running along the 'ms' coordimate axis.

Note that we're composing cumulate with an apply operator. SciDB's query
execution engine pipelines the data from the apply into the cumulate on an
as-needed basis. Finally, we divide the two running cumulative sums to get the
VWAP Remember, this quantity is computed for all the stocks!



## Inexact time join with last-value imputation

The example below shows the AFL query that joins trade
data with quote data. At time points where quote data is not available, the
last known value is looked up and filled in. This is sometimes called an
'as.of' join or 'last value carry forward' join.

The syntax is
```
iquery -aq "asof(quotes as A, trades as B, A.ms, B.ms)"
```
or if timestamp is the last dimension in the array, simply:
```
iquery -aq "asof(quotes, trades)"
```

Note that in the above syntax, it is assumed that there is no dummy / synthetic dimension to handle collisions on the timestamp dimension. The `quotes` and `trades` array used in this example do have a dummy dimension. We provide the following example script to handle this case:
```
./prepare_last_value_join.sh  "quote array or expression"  "trade array or expression"
```
The script aggregates out the dummy dimension from `quotes` and `trades` arrays and stores the results in `quotes_redim` and `trades_redim` arrays respectively. You can then feed these resultant arrays into the `asof` join.

Here is an example that preps the trades and quotes data for 'BAM'. We use the fact
that we know the symbol index for BAM is 615 from the last example. It takes
a short while to generate the temporary arrays that aggregate out the dummy dimension are generated (see the comments
in the script).

```
./prepare_for_last_value_join.sh "between(quotes, null,615,0, null,615,null)" "between(trades, null,615,0, null,615,null)"

# Count the result
iquery -aq "op_count(asof(quotes_redim, trades_redim))"

## {i} count
## {0} 4362


# This matches the count of the number of unique time elements for this
# instrument in the trades array:

iquery -aq "op_count(uniq(sort(project(apply(between(trades,null,615,null,null,615,null), time, string(ms)),time))))" 

## {i} count
## {0} 4362


# Show just part of the result
iquery -aq "asof(quotes_redim, trades_redim)" | head

## {symbol_index,ms} ask_price,bid_price,price,volume,sequence_number,condition,exchange
## {615,34185171} 41.6,37.8,38.9,91,3309,'  TI','P'
## {615,34185172} 41.6,37.8,39,100,3310,' FT ','T'
## {615,34185173} 41.6,37.8,38.8,91,3312,'  TI','T'
## {615,34185950} 42,37.8,38.8,9,3313,'  TI','T'
## {615,34200381} 40.1,37,39.8,9761,3695,'O   ','N'
## {615,34200429} 40.1,39.2,39.2,100,3742,' F  ','N'
## {615,34201201} 40.1,38.6,38.9,100,3899,' F  ','Y'
## {615,34201215} 40.1,38.4,38.8,100,3906,'Q   ','P'
## {615,34201216} 40.1,38.4,38.8,100,3907,' F  ','P'
```

Now you can also try the asof join on the entire day's data... this will take a little longer. 
```
./prepare_for_last_value_join.sh quotes trades
```

To get an idea of the sizes of the resultant array, let us run some counts
```
iquery -aq "op_count(quotes_redim)"

## {i} count
## {0} 93336911

iquery -aq "op_count(trades_redim)"

## {i} count
## {0} 22633275
```
Then you can run the asof join for the entire day's data using the same syntax as before
Note that this is a join of 93,336,911 quotes with 22,633,275 trades

```
iquery -aq "asof(quotes_redim, trades_redim)" | head

## {symbol_index,ms} ask_price,bid_price,price,volume,sequence_number,condition,exchange
## {0,34200011} 66.5,56.5,61,32051,2325,' O  ','N'
## {0,34201498} 61,60,60.1,30,2971,'I   ','N'
## {0,34207432} 60.8,59.7,60.025,100,3782,'@   ','D'
## {0,34207506} 60.8,59.7,60.1,100,3785,'@   ','B'
## {0,34210008} 61,59.7,60.8,100,4112,'Q   ','P'
## {0,34210009} 62,60.1,60.8,200,4114,' F  ','N'
## {0,34210306} 61,60.3,60.9,100,4168,'Q   ','T'
## {0,34210307} 61,60.3,60.8,100,4169,' F  ','N'
## {0,34210610} 61,59.7,60.8,100,4201,' F  ','N'
```

Or to time the asof join (Note that this depends almost entirely on the hardware configuration)
```
time iquery -aq "consume(asof(quotes_redim, trades_redim))"
```

## Violations of NBBO (Regulation NMS)

Next, let us run some interesting analysis on the result of the `asof` join. We can filter for the trades where the traded price was higher than the lowest ask. 

```
$ iquery -aq "filter(asof(quotes_redim, trades_redim), price > ask_price)" | head
{symbol_index,ms} ask_price,bid_price,price,volume,sequence_number,condition,exchange
{0,34232423} 59.4,60.7,60.9,100,5722,' F  ','P'
{0,34232424} 59.4,60.7,60.9,100,5724,' F  ','T'
{0,34240389} 59.4,61.1,61.3,100,6142,' F  ','T'
{0,34245395} 58.2,61.7,62,100,6324,' F  ','P'
{0,34246395} 0,61.6,62.2,400,6408,' F  ','N'
```

A count of such trades, and a count of the total number of trades:
```
$ iquery -aq "op_count(filter(asof(quotes_redim, trades_redim), price > ask_price))"
{i} count
{0} 1342671

$ iquery -aq "op_count(trades_redim)"
{i} count
{0} 22633275
```

Finally, a timing of running this analysis on all the data (93,336,911 quotes with 22,633,275 trades, run across 7500 tickers):
```
$ time iquery -aq "consume(filter(asof(quotes_redim, trades_redim), price > ask_price))"
Query was executed successfully

real	0m37.394s
user	0m0.011s
sys	0m0.003s
```

