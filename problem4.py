'''
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from helpers import runtime
from helpers.string import palindrome

def largest_palindrome_product():
    return max([n * m
                for n in range(100, 1000)
                for m in range(n, 1000)
                if palindrome(str(n * m))])

runtime.print_answer_and_elapsed_time(largest_palindrome_product)
