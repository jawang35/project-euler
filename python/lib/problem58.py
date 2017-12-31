'''
Problem 58 - Spiral Primes

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
'''

from functools import partial
from lib.helpers.numbers import is_prime
from lib.helpers.runtime import print_answer_and_elapsed_time


def spiral_primes_at_ratio(ratio):
    length = 1
    diagonal_number = 1
    diagonal_primes = 0

    while length == 1 or diagonal_primes / ((2 * length) - 1) > ratio:
        length += 2
        for _ in range(4):
            diagonal_number += length - 1
            if is_prime(diagonal_number):
                diagonal_primes += 1

    return length

answer = partial(spiral_primes_at_ratio, ratio=0.1)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
