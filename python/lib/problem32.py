# coding=utf-8
'''
Problem 32 - Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

from itertools import permutations
from lib.helpers.runtime import print_answer_and_elapsed_time


def pandigital_products(max_digits):
    assert 2 < max_digits < 10

    digits = range(1, max_digits + 1)
    sorted_digits = sorted(''.join([str(digit) for digit in digits]))
    product_length = int(max_digits / 2)
    equal_index = max_digits - product_length

    pandigital_product_results = set()
    for multiplication_index in range(1, int(equal_index / 2) + 1):
        for multiplicand_digits in permutations(digits, multiplication_index):
            possible_multiplier_digits = [digit
                                          for digit in digits
                                          if digit not in multiplicand_digits]
            multiplier_digits_permutations = permutations(
                possible_multiplier_digits,
                equal_index - multiplication_index)
            for multiplier_digits in multiplier_digits_permutations:
                multiplicand = int(''.join([str(digit)
                                   for digit in multiplicand_digits]))
                multiplier = int(''.join([str(digit)
                                 for digit in multiplier_digits]))
                product = multiplicand * multiplier
                current_sorted_digits = sorted(str(multiplicand) +
                                               str(multiplier) +
                                               str(product))
                if current_sorted_digits == sorted_digits:
                    pandigital_product_results.add(product)
    return pandigital_product_results


def answer():
    return sum(pandigital_products(9))

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
