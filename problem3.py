'''
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
from helpers import runtime
from helpers.math import sieve_of_eratosthenes

def largest_prime_factor():
    number = 600851475143
    sqrt_of_number = round(math.sqrt(number))
    sieve = sieve_of_eratosthenes(sqrt_of_number)
    for n in reversed(range(sqrt_of_number)):
        if sieve[n] and number % n == 0:
            return n
    return number

runtime.print_answer_and_elapsed_time(largest_prime_factor)
