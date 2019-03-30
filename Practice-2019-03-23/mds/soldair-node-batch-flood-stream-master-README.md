batch-flood-stream
=======================

emits batches of data events. grouped based on rate they are emitted and a max batch size.

```js
var stream = batch(ondata,options);
```
- ondata is optional
- options are optional
  - size: defaults to 10000 uses data.length or if objects the number of objects
  - wait: defaults to 1000 ms
  - stats: off. if you pass a truthy value batch arrays will have a delay and a rate property.


```js

  var s = batch({wait:5}).on('data',function(batch){
    console.log('data',batch);
  });

  var i = 0;
  var timer = setInterval(function(){
    s.write(++i);
    if(i == 50) {
      clearTimeout(timer);
      s.end();
    }
  },1);

```

outputs something like

```
data [ 1 ]
data [ 2 ]
data [ 3, 4 ]
data [ 5, 6, 7 ]
data [ 8 ]
data [ 9, 10, 11 ]
data [ 12, 13, 14, 15 ]
data [ 16, 17 ]
data [ 18, 19, 20 ]
data [ 21, 22, 23, 24 ]
data [ 25, 26 ]
data [ 27, 28, 29 ]
data [ 30, 31, 32 ]
data [ 33, 34, 35 ]
data [ 36, 37, 38, 39 ]
data [ 40, 41, 42 ]
data [ 43, 44, 45, 46 ]
data [ 47, 48, 49 ]

```

