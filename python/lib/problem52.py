'''
Problem 52 - Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

from functools import partial
from itertools import groupby
from lib.helpers.runtime import print_answer_and_elapsed_time


def number_to_string_of_digits(number):
    return ''.join(sorted(set(str(number))))


def permuted_multiples(largest_multiplier):
    x = 1
    multipliers = range(1, largest_multiplier + 1)

    while True:
        multiples = [multiplier * x for multiplier in multipliers]
        digit_groups = groupby(map(number_to_string_of_digits, multiples))

        if len(list(digit_groups)) == 1:
            return x

        x += 1

answer = partial(permuted_multiples, largest_multiplier=6)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
