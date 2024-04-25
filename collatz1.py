"""
collatz1.py - run a Collatz simulation on a given positive integer
Eric Conrad

LICENSE

    Copyright 2024 by Eric Conrad.

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software”), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject
    to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

USAGE

    Requires matplotlib.

    For usage:
        python collatz1.py -h

    General usage:
        python collatz1.py VALUE
"""

import argparse
import matplotlib.pyplot as plt

def simulate(n):
    """run a simulation assuming the conjecture is true"""
    if not isinstance(n, int):
        raise TypeError

    if n < 1:
        raise ValueError

    collatz_seq = []
    collatz_set = set()

        # Assume the Collatz conjecture is true
    while not n in collatz_set:
        collatz_seq.append(n)
        collatz_set.add(n)
        if n % 2:           # when n is odd:    n := 3n+1
            n = 3*n + 1
        else:               # when n is even:   n := n/2
            n = n // 2

    return collatz_seq

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collatz simulator")
    parser.add_argument("value", type=int, help="integer to plot")
    args = parser.parse_args()

    collatz = simulate(args.value)
    print(collatz)

    plt.plot(collatz)
    plt.title("Collatz sequence for %d" % args.value)
    plt.xlabel("n")
    plt.ylabel("a(n)")
    plt.show()
