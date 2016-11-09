'''
Problem 40 - Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import product

def champernowne_fractional_part(length):
    result = ''
    n = 1
    while len(result) < length:
        result += str(n)
        n += 1
    return result

def product_champernowne_digits(*args):
    constant = champernowne_fractional_part(max(args))
    return product([int(constant[digit - 1]) for digit in args])

answer = partial(product_champernowne_digits, 1, 10, 100, 1000, 10000, 100000, 1000000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
