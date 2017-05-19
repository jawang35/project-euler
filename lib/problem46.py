#coding=utf-8
'''
Problem 46 - Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a
prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from math import sqrt
from lib.helpers.numbers import is_prime
from lib.helpers.runtime import print_answer_and_elapsed_time

def smallest_non_goldbach_number():
    primes = [2]
    n = 1
    while True:
        n += 2
        if is_prime(n):
            primes.append(n)
        else:
            is_goldbach = False
            for p in primes:
                if sqrt((n - p) / 2).is_integer():
                    is_goldbach = True
                    break
            if not is_goldbach:
                return n

answer = smallest_non_goldbach_number

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
