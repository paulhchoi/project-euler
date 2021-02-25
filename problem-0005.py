"""
Solution to Project Euler problem 5
https://projecteuler.net/

    {title}

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

(c) Paul Choi 2021

Notes:
    Must be multiple of 20
    Brute force O(n²) sol
"""
from utils import format_solution_output


def run():

    init_steps = 20*19

    # knowing that the sol must be a multiple of 20*19,
    # use that as start and step increment
    # and check each divisibility of each increment from 20 to 1
    for num in range(init_steps, 2**32, init_steps):
        if is_divisible_by_all_in_range(20, 1, num):
            return num
    else:
        return False


def is_divisible_by_all_in_range(high, low, value):
    for x in range(high, low, -1):
        if value % x != 0:
            return False
    else:
        return True


if __name__ == "__main__":
    format_solution_output(5, run())
