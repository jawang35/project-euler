'''
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers.math import prime_divisors

def largest_prime_factor(number):
    return max(prime_divisors(number))

if __name__ == '__main__':
    print_answer_and_elapsed_time(partial(largest_prime_factor, number = 600851475143))
