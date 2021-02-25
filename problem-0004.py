"""
Solution to Project Euler problem 4
https://projecteuler.net/

    Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made from the product of two
    2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

(c) Paul Choi 2021

Notes:
    Brute force, O(n²) solution

"""
from utils import format_solution_output


def run():
    x = y = largest_pal = 0

    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            res = i * j
            if is_palindrome(res) and res > largest_pal:
                x = i
                y = j
                largest_pal = res

    else:
        return x, y, largest_pal


def is_palindrome(val):
    # convert value into char array
    val = list(str(val))

    start_ptr = 0
    end_ptr = len(val) - 1

    # set ptr to start and end of array, and compare to halfway point
    for x in range(0, end_ptr):
        if start_ptr > end_ptr:
            return True

        if val[start_ptr] != val[end_ptr]:
            return False
        else:
            start_ptr += 1
            end_ptr -= 1

    return True


if __name__ == "__main__":
    format_solution_output(4, run())
