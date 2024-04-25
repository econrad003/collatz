"""
collatz3.py - test the Collatz conjecture for a range of values
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

    This module imports several items from collatz2.py.

    Essentially it tests a range of values against the Collatz conjecture.
    If the Collatz conjecture fails for any value in the range, then (in
    principle) the program will enter an infinite loop.  (See documentation
    for collatz2.py for more information.

    If the run is successful (i.e. if no exceptions to the conjecture are
    encountered), then the table is displayed.  Sequences and other data
    may be recovered using the tabulated information.

USAGE

    For usage help:
        python3 collatz3.py -h

    Basic usage:
        python3 collatz3.py START_VALUE STOP_VALUE
"""

import argparse
import collatz2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collatz range simulator")
    parser.add_argument("range_values", type=int, nargs="*",
                        help="integer range to test")
    parser.add_argument("-D", "--doc", action="store_true",
                        help="display the documentation and exit")
    parser.add_argument("-L", "--license", action="store_true",
                        help="display the license and exit")

#       This program behaves like collatz2 with the verbose option
#    parser.add_argument("-v", "--verbose", action="store_true",
#                        help="display the contents of the table")
    args = parser.parse_args()

    if args.doc:
        print(__doc__)
        exit()
    if args.license:
        collatz2.license()

    values = range(*args.range_values)
    for key in values:
        collatz2.simulate(key, False)

    print("         N     length    maximum     second")
    print("---------- ---------- ---------- ----------")
    collatz = collatz2.collatz
    keys = sorted(collatz.keys())
    for key in keys:
        lgth, largest, second, note = collatz[key]
        print("%10d %10d %10d %10d" % (key, lgth, largest, second), note)
