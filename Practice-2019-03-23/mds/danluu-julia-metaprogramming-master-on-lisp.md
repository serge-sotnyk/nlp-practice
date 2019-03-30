# Notes from On Lisp

Just reading On Lisp and working through it in Julia. Nothing to see here

## 2.2 Defining functions
In lisp we can #' to get the definition of a function
~~~
> (defun double (x) (* x 2))
> #’double
#<Interpreted-Function C66ACE>
~~~

In julia,
~~~
> function double(x) x*2 end
> double
double (generic function with 1 method)
> code_typed(double,(Int,))                                                                                                    
1-element Array{Any,1}:
 :($(Expr(:lambda, {:x}, {{},{{:x,Int64,0}},{}}, quote  # none, line 1:
        return top(box)(Int64,top(mul_int)(x::Int64,2))::Int64
    end)))
~~~

## 2.3 Functional Arguments
Has apply, just like lisp. Unlike CL, you don't even have to quote symbols!
~~~
> apply(+, 1, 2)
3
~~~

Functions can take functions
~~~
> sort([1,2,3,-1,-2], by=abs)
~~~

If filter didn't exist, we'd have to write it
~~~
function filter(f::Function, a::Vector)
    r = Array(eltype(a), 0)
    for i = 1:length(a)
        if f(a[i])
            push!(r, a[i])
        end
    end
    return r
end
~~~

## 2.4 Functions as Properties
Multiple dispatch example here???

## 2.5 Scope
~~~
julia> y = 7
7
~~~

~~~
julia> function plusy(x)
         x + y
       end
plusy (generic function with 1 method)

julia> plusy(0)
7

julia> y = 10
10

julia> plusy(0)
10

julia> function hasy()
         y = 3
         plusy(0)
       end
hasy (generic function with 1 method)

julia> hasy
hasy (generic function with 1 method)

julia> hasy()
10
~~~

julia has a let block! Can use it to copy example
~~~
julia> let y = 22
         function plusy(x)
           x + y
         end
       end
plusy (generic function with 1 method)

julia> plusy(3)
25

julia> let y = 100
         plusy(3)
       end
25
~~~

## 2.6 Closures
Can we do this? Apparently not.

~~~
julia> let counter = 0
         function new_id()
           counter += 1
         end
         function reset_id()
           counter = 0
         end
       end
reset_id (generic function with 1 method)

julia> new_id
ERROR: new_id not defined
~~~

How is it that the above `let / plusy` example works but this doesn't?

> Does this count?

~~~
function make_counter()
          counter = 0            
          (function ()
                  counter += 1
          end,               
          function ()
                  counter = 0
          end)
end 

~~~

Usage:

~~~
julia> (new_id,reset_id) = make_counter()
((anonymous function),(anonymous function))

julia> reset_id()
0

julia> new_id()
1

julia> new_id()
2

julia> new_id()
3

julia> reset_id()
0

julia> reset_id()
0

julia> new_id()
1

julia> new_id()
2

julia> new_id()
3

~~~


### Example 2:
~~~
julia> function make_adder(n)
         (x -> x + n)
       end
make_adder (generic function with 1 method)

julia> a = make_adder(3)
(anonymous function)

julia> a(3)
6

julia> a(4)
7
~~~

Next example uses optional arguments. How should we do that? Is https://github.com/JuliaLang/Options.jl the right way?

For example in Figure 2.1, what's a Julian way to do it?

## 2.7 Local Functions

Comment on how let doesn't see previous let values, so you need labels, doesn't apply
~~~
julia> let x = 10, y = 2 * x
         println(x); println(y)
       end
10
20

function count_instances (obj, lsts)
  let instances_in = (lst ->
    ...      
~~~

Would we ever do this in julia, rather than iterating?

## 2.8 Tail recursion

Julia doesn't optmize this! Maybe do some examples of trampolining?

## 2.9 Compilation

Not really relevant. Could play with JIT here

## 2.10 Functions from Lists

Not relevant.

# Chapter 3: functional programming

## 3.1 Functional Design

Some comments on why functional programming is better

