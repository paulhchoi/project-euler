"""
Solution to Project Euler problem 1
https://projecteuler.net/

    Multiples of 3 and 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

(c) Paul Choi 2021
"""
from utils import format_solution_output


def run():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


if __name__ == "__main__":
    format_solution_output(1, run())
