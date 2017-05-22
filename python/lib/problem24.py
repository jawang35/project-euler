'''
Problem 24 - Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time
from math import factorial


def nth_lexicographic_permutations(digits, permutation):
    sorted_digits = sorted(digits)
    result = ''
    permutations_remaining = permutation - 1
    for i in range(len(digits)):
        permutations_at_digit = factorial(len(digits) - 1)
        digit_to_append = int(permutations_remaining / permutations_at_digit)
        result += str(digits.pop(digit_to_append))
        permutation -= 1
        permutations_remaining -= permutations_at_digit * digit_to_append
    return result

answer = partial(nth_lexicographic_permutations,
                 digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 permutation=1000000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
