'''
Problem 9 - Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math
from functools import partial
from helpers import runtime

def special_pythagorean_triplet(sum):
    numbers_to_sum = range(1, sum)
    for a in numbers_to_sum:
        for b in numbers_to_sum:
            c = math.sqrt(a**2 + b**2)
            if a + b + c == sum:
                return int(a * b * c)
    return 0

if __name__ == "__main__":
    runtime.print_answer_and_elapsed_time(partial(special_pythagorean_triplet, 1000))
