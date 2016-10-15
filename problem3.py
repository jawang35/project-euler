'''
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
from functools import partial
from helpers import runtime
from helpers.math import sieve_of_eratosthenes

def largest_prime_factor(number):
    sqrt_of_number = math.floor(math.sqrt(number)) + 1
    factor = 1
    for n in range(2, sqrt_of_number):
        if number % n == 0:
            factor = n
            break
    if factor == 1:
        return number
    return max(largest_prime_factor(factor), largest_prime_factor(number / factor))

if __name__ == "__main__":
    runtime.print_answer_and_elapsed_time(partial(largest_prime_factor, number = 600851475143))
