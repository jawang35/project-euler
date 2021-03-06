'''
Problem 7 - 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time
from lib.helpers.numbers import sieve_of_eratosthenes, is_prime


def nth_prime_number(number):
    count = 0
    n = 1
    while count < number:
        n += 1
        if is_prime(n):
            count += 1
    return n

answer = partial(nth_prime_number, number=10001)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
