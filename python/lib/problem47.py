#coding=utf-8
'''
Problem 47 - Distinct Prime Factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first
of these numbers?
'''

from lib.helpers.numbers import prime_divisors
from lib.helpers.runtime import print_answer_and_elapsed_time

def consecutive_integers_with_distinct_primes(number_of_integers, number_of_distinct_primes):
    current_starting_integer = 2
    while True:
        found_starting_integer = True
        for n in range(number_of_integers):
            distinct_primes = set(prime_divisors(current_starting_integer + n))
            if len(distinct_primes) < number_of_distinct_primes:
                found_starting_integer = False
                current_starting_integer += n + 1
                break
        if found_starting_integer:
            return [current_starting_integer + n for n in range(number_of_integers)]

def answer():
    return consecutive_integers_with_distinct_primes(4, 4)[0]

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
