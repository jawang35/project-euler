'''
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers.string import is_palindrome

def largest_palindrome_product(minimum, maximum):
    return max([n * m
                for n in range(minimum, maximum)
                for m in range(n, maximum)
                if is_palindrome(str(n * m))])

if __name__ == '__main__':
    print_answer_and_elapsed_time(partial(largest_palindrome_product, minimum = 100, maximum = 1000))
