'''
Problem 30 - Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their
digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time

def number_is_sum_power_of_digits(number, power):
    return sum([int(digit)**power for digit in list(str(number))]) == number

def sum_powers_of_digits(power):
    digits = 1
    largest_number_with_digits = 0
    largest_sum_of_power = 0
    while True:
        largest_number_with_digits += 9 * 10**(digits - 1)
        largest_sum_of_power = digits * (9**power)
        if largest_number_with_digits >= largest_sum_of_power:
            break
        digits += 1

    return sum([n
                for n in range(10, largest_sum_of_power)
                if number_is_sum_power_of_digits(n, power)])

answer = partial(sum_powers_of_digits, power = 5)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
