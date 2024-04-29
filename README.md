# Collatz conjecture test programs (just for fun)

A Collatz sequence is a sequence of positive integers that obeys just two simple rules:
+ if a given term is even, the term that follows is half the given term;
+ if a given term is odd, then the terms that follows is the successor of three times the given term.

For example, the Collatz sequence starting with 3 is:
+ 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...

The Collatz conjecture states that the tail of every Collatz sequence is the 3-cycle \(4, 2, 1\).  Although simple to state, and although the conjecture has been tested for all integers with fewer than 20 digits, it has not been proven, nor have any exceptions been found.  There is more information available in Wikipedia.  A short summary of some results can be found in the documentation for *collatz2.py*. 

Posted here are some Python programs and some sample output.

The programs are released under an MIT-style license.

## Python programs:
+ collatz1.py - a program to plot a Collatz sequence \(requires matplotlib\)
+ collatz2.py - a utility which can be used to produce some data about some Collatz sequences
+ collatz3.py - a utitily which can be used to data for a range of Collatz sequences

## Data:
+ collatz_\*.png - plots of some interesting Collatz sequences
+ collatz*.txt - experimental output

## Status:
+ 29 April 2024 - All code has been tested and should work using a reasonably up-to-date Python (version 3) interpreter.  *Matplotlib* is required for collatz1.py.  All three scripts (collatz1.py, collatz2.py, collatz3.py) use *argparse* (part of the standard Python distribution) for command line parsing.  For script usage help, use the -h option, *e.g.*:
```python3 collatz1.py -h```

## Usage:
### collatz1.py
__usage:__ python3 collatz1.py \[-h\] value

Collatz simulator

__positional arguments:__
+ value
+ + integer to plot

__options:__
+ -h, --help
+ + show this help message and exit

__example:__
> `python3 collatz1.py 27` - plots the Collatz sequence for 27 starting with the first value 27 and ending with the first occurrence of the value 1.

### collatz2.py
__usage:__ python3 collatz2.py \[-h\] \[-D\] \[-L\] \[-v\] \[-s\] \[values ...\]

Collatz simulator

__positional arguments:__
+ values
+ + integers to test

__options:__
+ -h, --help
+ + show this help message and exit
+ -D, --doc
+ + display the documentation and exit
+ -L, --license
+ + display the license and exit
+ -v, --verbose
+ + display the contents of the table
+ -s, --stack
+ + display the stack for each computed value

__examples:__
> `python3 collatz2.py -v 27 255` - test values 27 and 255, and display the resulting table.

> `python3 collatz2.py -s 27 255` - test values 27 and 255, displaying heads of the resulting Collatz sequences. Table entries for 27 and 255 are displayed on completion.
+ output for `python3 collatz2.py -s 5 10`
```
$ python collatz2.py -s 5 10
1 [5, 16]
2 [10, 5]
3          N     length    maximum     second
4 ---------- ---------- ---------- ----------
5          5          6         16         16 odd
6         10          7         16          5 even
```
+ Lines 1 and 2 show the heads of the Collatz sequences.  Since 16 is a power of 2, the rest of the sequence for 5 is easy:
+ + 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...
+ In the case of 10, the head stops after 5, since 5 has already been encountered:
+ + 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...
+ In line 5, the length is 6 (for \[5, 16, 8, 4, 2, 1\] stopping before the first repeated value).  The maximum is 16, the largest value encountered in the sequence.  16 is also the second value encountered.  The note at the end indicates that the value 16 was obtained using the _odd_ rule (multiply by 3 and then add 1).  The possible rules are "odd", "even", or "power of two".  The power of two rule is just a special case of the even rule -- powers of two are handled programmatically in a special way.

### collatz3.py
__usage__: python3 collatz3.py \[-h\] \[-D\] \[-L\] \[range_values ...\]

Collatz range simulator

__positional arguments:__
+ range_values
  + integer range to test

__options:__
+ -h, --help
  + show this help message and exit
+ -D, --doc
  + display the documentation and exit
+ -L, --license
  + display the license and exit

__examples:__
> `python3 collatz3.py 3 50` - test values from 3 through 49, inclusive, and display the resulting table

> `python3 collatz3.py 3 30 5` - test values 3, 8, 13, 18, 23, 28
+ Entered values are used as parameters in a Python range. The above examples use `range(3,50)` and `range(3,30,5)`.  The output is similar to `collatz2.py` using the --verbose option.
