'''
Problem 34 - Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial
from lib.helpers.runtime import print_answer_and_elapsed_time

def sum_digit_factorial(number):
    return sum([factorial(int(digit)) for digit in str(number)])

def digit_factorials():
    maximum = 50000 # 10000000 is an analytical upper bound since 9999999 > 7 * 9!
    return [n for n in range(10, maximum) if sum_digit_factorial(n) == n]

def answer():
    return sum(digit_factorials())

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
