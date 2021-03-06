# coding=utf-8
'''
Problem 20 - Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time
from math import factorial


def factorial_digit_sum(number):
    return sum([int(digit) for digit in str(factorial(number))])

answer = partial(factorial_digit_sum, number=100)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
