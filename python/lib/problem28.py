'''
Problem 28 - Number Spiral Diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31


What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time


def sum_spiral_diagonals(size):
    assert size % 2 == 1
    sum = 1
    n = 1
    radius = 1
    while n < size**2:
        for _ in range(4):
            n += 2 * radius
            sum += n
        radius += 1
    return sum

answer = partial(sum_spiral_diagonals, size=1001)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
