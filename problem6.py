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

from helpers import runtime

def sum_square_difference():
    number = 100
    sum = 0
    for n in range(1, 101):
        for m in range(1, 101):
            if n != m:
                sum += n * m
    return sum

runtime.print_answer_and_elapsed_time(sum_square_difference)
