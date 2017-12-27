'''
Problem 51 - Prime Digit Replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
'''

from operator import itemgetter
from itertools import groupby
from lib.helpers.numbers import is_prime
from lib.helpers.runtime import print_answer_and_elapsed_time


def prime_digit_replacement_family(family_size):
    primality_map = {}
    number = 0

    while True:
        number_string = str(number)
        digit_counts = sorted(
            [(int(digit), len(list(group)))
             for (digit, group) in groupby(number_string)],
            key=itemgetter(1),
            reverse=True,
        )

        largest_count = digit_counts[0][1]

        digits_to_replace = (digit_count[0]
                             for digit_count in digit_counts
                             if digit_count[1] == largest_count)

        for digit in digits_to_replace:
            family = (int(''.join([str(n) if int(d) == digit else d
                                   for d in number_string]))
                      for n in range(10))
            family_primality_pre_check = (p
                                          for p in family
                                          if p not in primality_map or
                                          primality_map[p])
            family_primality = [(n, is_prime(n))
                                for n in family_primality_pre_check
                                if len(str(n)) == len(number_string)]
            prime_family = [n[0]
                            for n in family_primality
                            if n[1]]

            for (n, primality) in family_primality:
                primality_map[n] = primality

            if len(prime_family) >= family_size:
                return prime_family

        number += 1


def answer():
    return sorted(prime_digit_replacement_family(8))[0]

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
