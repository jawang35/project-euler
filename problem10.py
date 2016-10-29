'''
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers.math import sieve_of_eratosthenes

def summation_of_primes(maximum):
    sieve = sieve_of_eratosthenes(maximum)
    sum = 0
    for n, is_prime in enumerate(sieve):
        if is_prime:
            sum += n
    return sum

if __name__ == '__main__':
    print_answer_and_elapsed_time(partial(summation_of_primes, maximum = 2000000))
