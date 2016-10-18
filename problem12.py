'''
Problem 12 -
'''

from functools import partial
from helpers import runtime
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

if __name__ == "__main__":
    runtime.print_answer_and_elapsed_time(partial(highly_divisible_triangular_number, number_of_divisors = 500))
