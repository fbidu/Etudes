# Starting Out

## Numbers
* Expressions must end witha period followed by a whitespace (like a line break)
* You can separate expressions with commas, all will be evaluated, only the last will be shown
```
1> 2 + 15.
17
2> 49 * 100.
4900
3> 1892 - 1472.
420
4> 5 / 2.
2.5
5> 5 div 2.
2
6> 5 rem 2.
1
```
* `div` is the integer-to-integer division
* `rem` is the modulo - as in 'remainder'
* As expected, you can use serveral operators in one expression, they follow the usual precedence
* You can pass integers in other bases using the `Base#Value` syntax
```
1> 2#101010.
42
2> 16#f
15
```

## Invariable Variables
* "Variables" don't change value in functional programming
* Variable's names must begin with an uppercase letter
* Example from the book:
```
1> One.
* 1: variable 'One' is unbound
2> One = 1.
1
3> Un = Uno = One = 1.
1
4> Two = One + One.
2
5> Two = 2.
2
6> Two = Two + 1.
** exception error: no match of right hand side value 3
7> two = 2.
** exception error: no match of right hand side value 2
```
* You can assign a value to a variable ONLY ONCE
* How is that for "variable"?
* At first `One` is unbound, it has no value attached
* Then we attach 1 to `One`
* After `One` is attached to 1, when we do `0ne = some_value` the `=` operator acts as comparison
* If `some_value` is equal to `One`, Erlang will print the value. Otherwise it will complain
```
1> 20 = 15 + 5.
20
2> 20 = 10 + 11.
** exception error: no match of right hand side value 21
```
* `_` acts as a temporary variable
```
1> _ = 10 + 1.
11
2> _.
* 1: variable '_' is unbound
```
* `f(X).` unbounds a variable. `f().` unbounds all of them
* You can only use this resource at shells

## Atoms

* Atoms are variables whose value are the same as their names
```
1> atom.
atom
2> hai.
hai
3> 'Atoms can start with an uppercase letter if you surround it by single quotes'.
'Atoms can start with an uppercase letter if you surround it by single quotes'
4> hey@how_are_you.
hey@how_are_you
5> ab = 'ab'.
ab
6> 'ab' = ab.
ab
```
> The atom cat means "cat" and that's it. You can't play with it, you can't change it, you can't smash it to pieces; it's cat. Deal with it.
> An atom is therefore mainly useful to express or qualify data coupled with it. Used alone, it's a bit harder to find a good use to it. This is why we won't spend more time toying with them; their best use will come when coupled with other types of data.
* **Warnings**
	1. An atom is referenced on an 'atom table' that is *not* garbage collected
	2. They accumulate!
	3. Do *not* generate them dinamically
	4. They are tools for the developer!

