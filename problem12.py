'''
Problem 12 - Highly Divisible Triangular Number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers import math

def highly_divisible_triangular_number(number_of_divisors):
    triangle_number = 0
    index = 0
    while True:
        index += 1
        triangle_number += index
        divisors = math.divisors(triangle_number)
        if len(divisors) > number_of_divisors:
            return triangle_number

if __name__ == '__main__':
    print_answer_and_elapsed_time(partial(highly_divisible_triangular_number, number_of_divisors = 500))
