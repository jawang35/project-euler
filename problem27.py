#coding=utf-8
'''
Problem 27 - Quadratic Primes

Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41**2 + 41 + 41n = 41, is clearly divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n=0.
'''

from math import sqrt
from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import is_prime

def maximum_quadratic_primes(maximum):
    minimum = -maximum
    result = (0, 0)
    maximum_consecutive_primes = 0
    for a in range(minimum + 1, maximum):
        for b in range(max(0, 1 - a), maximum + 1):
            n = 0
            while is_prime(n**2 + (a * n) + b):
                n += 1
                if n > maximum_consecutive_primes:
                    result = (a, b)
                    maximum_consecutive_primes = n
    return result

def answer():
    coefficients = maximum_quadratic_primes(1000)
    return coefficients[0] * coefficients[1]

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
