'''
Problem 49 - Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual
in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are
permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from itertools import permutations
from helpers.numbers import sieve_of_eratosthenes
from helpers.runtime import print_answer_and_elapsed_time

def prime_permutations(number_of_digits):
    minimum = 10**(number_of_digits - 1)
    maximum = 10 * minimum
    sieve = sieve_of_eratosthenes(maximum)
    permutation_list = []
    permutations_accounted_for = set()
    for prime in [p for p in range(minimum, maximum) if sieve[p]]:
        if prime in permutations_accounted_for:
            continue
        digit_permutations = set([int(''.join(permutation))
                                  for permutation in permutations(str(prime), number_of_digits)])
        prime_digit_permutations = [p
                                    for p in digit_permutations
                                    if sieve[p] and prime <= p < maximum]
        permutations_accounted_for.update(prime_digit_permutations)
        permutation_list.append(sorted(prime_digit_permutations))
    return [permutation for permutation in permutation_list if len(permutation) > 2]

def find_three_term_sequences(ordered_permutations):
    sequences = []
    for permutation in ordered_permutations:
        for i, term1 in enumerate(permutation):
            for j, term2 in enumerate(permutation[i+1:]):
                if [s for s in sequences if s[0] == term1 and s[1] == term2]:
                    continue
                term3 = 2 * term2 - term1
                if term3 in permutation:
                    sequences.append([term1, term2, term3])
    return sequences

def prime_permutation_sequences(number_of_digits):
    return find_three_term_sequences(prime_permutations(number_of_digits))

def answer():
    return int(''.join(str(p) for p in prime_permutation_sequences(4)[1]))

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
