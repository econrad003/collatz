"""
collatz2.py - run a Collatz simulation on a given positive integer
Eric Conrad

LICENSE

    Copyright 2024 by Eric Conrad.

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    “Software”), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject
    to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

DESCRIPTION

    A Collatz sequence is a sequence of positive integers that satisfies
    the following recurrence relation:
        (1)  a_(k+1) = 3a_k + 1 whenever a_k is odd and
        (2)  a_(k+1) = a_k / 2 whenever a_k is even.

    If a_0 is 1, then the sequence is 3-periodic:
        (3)  1, 4, 2, 1, 4, 2, 1, 4, 2, ...

    If a_0 is a power of 2, i.e. if a_0=2^n, then a_(n+1) is 1, and the
    (n+1) tail of the sequence is the 3-periodic sequence given in
    display (3).  For example, with n=4, we have a_0=2^4=16 giving the
    Collatz sequence:
        (4)  16, 8, 4, 2, 1, 4, 2, 1, ...

    For other numbers, the sequence is more complicated.  For example,
    for a_0=3:
        (5)  3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, ...
    After 3 iterations, the sequence reaches a power of 2, namely 16,
    and then it becomes clear that the sequence has a 3-periodic tail
    with terms 1, 4, and 2.

    The Collatz sequence for a_0=5 is found in the 2-tail of the sequence
    for a_0=3:
        (6)  5, 16, 8, 4, 2, 1, ...

    We give just three more sequences as illustrations.  For a_0=6:
        (7)  6, 3, 10, 5, 16, ...
    Here we arrive at 16 with four iterations.  For a_0=7, we have:
        (8)  7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, ...
    Since we encountered 10 in display (7), we know that the Collatz
    sequence for 10 eventually ends with the standard 3-cycle 1,
    4, 2 sequence.  Note also the peaks that follow the odd numbers:
        (8a) 22, 34, 52, 40, 16, 4, 4, 4, ...

    Finally, here is the sequence for a_0=27:
        (9)  27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107,
             322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412,
             206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263,
             790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334,
             167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276,
             638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619,
             4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102,
             2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
             866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184,
             92, 46, 23, 70, 35, 106, 53, 160, 80, 40, ...
    The sequence bounces up and down, reaching a global maximum of
    9232.  Eventually it reaches a value of 40, which we already
    encountered in the Collatz sequence for 7, so we know that this
    sequence has the usual 3-cycle tail.

CONJECTURE

    The Collatz conjecture simply states that all Collatz sequences
    end with the 3-periodic 1, 4, 2 tail.  At this point in time,
    the conjecture has not been proven, nor has it been disproven.
    The conjecture is known to hold for all postive integers up
    to and including 2^68 (a 21-digit number).  In addition, there
    are some known upper bounds on the density of exceptions. [1]

    In addition, if there is an exception which ends in some other
    cycle, then that cycle would have at least 186,265,759,595
    (~ 186 billion) terms. [1]

IMPLEMENTATION

    This program implements a table which is seeded with powers of two
    up through 2^20.  As values are encountered, the are added to the
    table.  The Collatz sequence for any encountered value can be
    reconstructed from the table.  (The --verbose option displays the
    tabulated information.  The --stack option displays the heads of
    requested sequences.  If neither option is specified, table entries
    for requested values are displayed.)  To illustrate the workings,
    we consider the command:
        python3 collatz2 -s 3

    We start with the value 3.  It is not in the table, so we push in
    down onto the stack.  It is odd, so the next term is 10.  Since 10
    is not in the table, we push it as well.  We do likewise for the
    third term 5.  The fourth term is the seed value 16 (a power of two)
    which is in the table.

    Since the stack option was specified (using the short form -s), we
    display the stacked values and the first encountered value:
        [3, 10, 5, 16]

    We now must add the new values to the table.  The table entry for
    16 tells us that its next term is 8, its peak is 16, and the length
    to reach 1 is 5 (i.e. [16, 8, 4, 2, 1] -- a list of 5 terms.)

    We pop 5.  Its next term is 16, the length to 1 is 6 (1 more than
    the length from 16 to 1), and the peak is 16 (the maximum of 5 and
    the peak value of 16).

    We pop 10.  (Next: 5, Length: 6+1=7, Peak: max(10, peak(5))=16).

    We pop 3.  (Next: 10, Length: 8, Peak: 16).

    Since the --verbose option was not specified, we only display the
    table entries for requested values, namely 3.

                 N     length    maximum     second
        ---------- ---------- ---------- ----------
                 3          8         16         10 odd

    Using a typical terminal, the full exchange will look like this:

        > python3 collatz2.py -s 3
        [3, 10, 5, 16]
                 N     length    maximum     second
        ---------- ---------- ---------- ----------
                 3          8         16         10 odd

    If we had used the --verbose option, we would see more detail:

        > python3 collatz2.py -s -v 3
        [3, 10, 5, 16]
                 N     length    maximum     second
        ---------- ---------- ---------- ----------
                 1          1          1          4 power of two
                 2          2          2          1 power of two
                 3          8         16         10 odd
                 4          3          4          2 power of two
                 5          6         16         16 odd
                 8          4          8          4 power of two
                10          7         16          5 even
                16          5         16          8 power of two
                32          6         32         16 power of two
                64          7         64         32 power of two
                   [...snip...]
            524288         20     524288     262144 power of two
           1048576         21    1048576     524288 power of two

    If a value larger than 2^20 is encountered, then larger powers
    two are added as seeds to extend the table.

BUGS

    Exceptions, if any, to the Collatz conjecture will (in principle) result
    in infinite loops.  In practice, available memory will be exhausted.

    In principle, a periodic exception could be detected by maintaining a
    dictionary containing stack entries, but the extra overhead is not
    justified in practice.  (The minimum value in and the length of a
    minimum exception cycle (i.e. a cycle other than [1 4 2]) make
    detection impractical using current hardware.)

    This program cannot, either in principle or in practice, detect an
    aperiodic exception.  Note that the "limite supérieure" (limsup) of
    such an exception is necessarily infinite.

REFERENCES

    [1]  "Collatz conjecture" in Wikipedia, 21 Apr. 2024. Web.
         Accessed 22 Apr. 2024. 

USAGE
    For usage information, run with -h or --help option, e.g.:
        python3 collatz2 -h
    To display this documentation, run with -D or --doc, e.g.:
        python3 collatz2 -D

MODIFICATION HISTORY
    collatz1 - 20 April 2024
        Initial version.  Options --stack and --verbose were implemented.
    collatz2 - 22 April 2024
        Added documentation.  Added --doc and --license options.
"""

import argparse

collatz = {}    # [length, maximum, next, note]

# For a power n=2^k of 2, the length of the Collatz sequence for n is k+1
# and the maximum value reached in n.  We initialize the table with powers
# 2 up to 2^20.

n, k = 1, 0
note = "power of two"
while k < 21:
    k += 1
    collatz[n] = [k, n, (4 if n==1 else n//2), note]
    n += n
assert collatz[1] == [1, 1, 4, note]
assert collatz[2] == [2, 2, 1, note]
assert collatz[4] == [3, 4, 2, note]

next_n = n
next_k = k
next_note = note

def extend_powers(current_n):
    """add more powers of two"""
    while next_n < current_n:
        next_k += 1
        collatz[next_n] = [next_k, next_n, next_n // 2, next_note]
        next_n += next_n

def simulate(n, show_stack):
    """run a simulation assuming the conjecture is true"""
    if not isinstance(n, int):
        raise TypeError

    if n < 1:
        raise ValueError

    stack = []
    while not n in collatz:
        if n > next_n:
            extend_powers(n)
            continue
        stack.append(n)
        if n % 2:           # odd
            n = 3*n + 1
        else:               # odd
            n = n // 2

    if show_stack:
        full_stack = stack + [n]
        print(full_stack)

    lgth, largest, _, _ = collatz[n]
    while stack:
        second = n
        n = stack.pop()
        lgth += 1
        largest = max(n, largest)
        collatz[n] = [lgth, largest, second, ("odd" if n%2 else "even")]

def license():
    """display the license"""
    print("""
collatz2.py - run a Collatz simulation on a given positive integer
Eric Conrad

LICENSE

    Copyright 2024 by Eric Conrad.

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    “Software”), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject
    to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    """)
    exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collatz simulator")
    parser.add_argument("values", type=int, nargs="*", help="integers to test")
    parser.add_argument("-D", "--doc", action="store_true",
                        help="display the documentation and exit")
    parser.add_argument("-L", "--license", action="store_true",
                        help="display the license and exit")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="display the contents of the table")
    parser.add_argument("-s", "--stack", action="store_true",
                        help="display the stack for each computed value")
    args = parser.parse_args()

    if args.doc:
        print(__doc__)
        exit()

    if args.license:
        license()

    for key in args.values:
        simulate(key, args.stack)

    print("         N     length    maximum     second")
    print("---------- ---------- ---------- ----------")
    keys = sorted(collatz.keys()) if args.verbose or len(args.values) == 0 \
        else args.values
    for key in keys:
        lgth, largest, second, note = collatz[key]
        print("%10d %10d %10d %10d" % (key, lgth, largest, second), note)

