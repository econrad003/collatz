# collatz
Collatz conjecture test programs (just for fun)

A Collatz sequence is a sequence of positive integers that obeys just two simple rules:
+ if a given term is even, the term that follows is half the given term;
+ if a given term is odd, then the terms that follows is the successor of three times the given term.

For example, the Collatz sequence starting with 3 is:
+ 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...

The Collatz conjecture states that the tail of every Collatz sequence is the 3-cycle \(4, 2, 1\).  Although simple to state, and although the conjecture has been tested for all integers with fewer than 20 digits, it has not been proven, nor have any exceptions been found.  There is more information available in Wikipedia.  A short summary of some results can be found in the documentation for *collatz2.py*. 

Posted here are some Python programs and some sample output.

Python programs:
+ collatz1.py - needs to be tested! - a program to plot a Collatz sequence \(requires matplotlib\)
+ collatz2.py - tested - a utility which can be used to produce some data about some Collatz sequences
+ collatz3.py - tested - a utitily which can be used to data for a range of Collatz sequences

Data:
+ collatz_\*.png - plots of some interesting Collatz sequences
+ collatz*.txt - experimental output

Most of the code in collatz1.py has been tested in some online interpreters, but the program still needs testing in a command-line environment.
