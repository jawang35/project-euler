'''
Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the
square of the sum.
'''

from functools import partial
from helpers import runtime

def sum_square_difference(number):
    natural_numbers = range(1, number + 1)
    sum = 0
    for n in natural_numbers:
        for m in natural_numbers:
            if n != m:
                sum += n * m
    return sum

if __name__ == "__main__":
    runtime.print_answer_and_elapsed_time(partial(sum_square_difference, number = 100))
