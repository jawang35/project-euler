'''
Problem 56 - Powerful Digit Sum

A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
'''

from lib.helpers.runtime import print_answer_and_elapsed_time


def digital_sum(number):
    return sum([int(digit) for digit in str(number)])


def answer():
    return max([digital_sum(a ** b) for a in range(100) for b in range(100)])

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
