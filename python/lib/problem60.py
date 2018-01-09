'''
Problem 60 - Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

from itertools import combinations_with_replacement
from lib.helpers.numbers import sieve_of_eratosthenes


def prime_pair_sets(set_size):
    primes = sieve_of_eratosthenes(1000000)
    sets = combinations_with_replacement(primes, r=set_size)

    i = 0
    for candidate_set in sets:
        print(candidate_set)

    # return ((p1, p2, p3, p4) for p1 in primes for p2 in primes for p3 in primes for p4 in primes)
    # print(primes)


def answer():
    primes = sieve_of_eratosthenes(1000)
    prime_list = list(primes)

    for i1, p1 in enumerate(prime_list):
        for i2, p2 in enumerate(prime_list[i1 + 1:], start=i1 + 1):
            for i3, p3 in enumerate(prime_list[i2 + 1:], start=i2 + 1):
                for i4, p4 in enumerate(prime_list[i3 + 1:], start=i3 + 1):
                    
