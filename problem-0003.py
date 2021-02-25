"""
Solution to Project Euler problem 3
https://projecteuler.net/

    Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

(c) Paul Choi 2021

TODO try sieve of eratosthenes next
"""
import math
from utils import format_solution_output


def run():
    val = 600851475143
    largest_prime = -1

    # iterate thru all factors of value
    for i in range(2, math.ceil(math.sqrt(val))):
        if val % i == 0 and is_prime(i):
            if i > largest_prime:
                largest_prime = i

    return largest_prime


def is_prime(val):
    # check if has factors
    for i in range(2, math.ceil(math.sqrt(val))):
        if val % i == 0:
            # if factor has factor, not prime, break
            return False
    else:
        return True


if __name__ == "__main__":
    format_solution_output(3, run())
