'''
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time
from lib.helpers.numbers import sieve_of_eratosthenes

def summation_of_primes(maximum):
    return sum(sieve_of_eratosthenes(maximum))

answer = partial(summation_of_primes, maximum = 2000000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
