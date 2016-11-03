'''
Problem 26 - Reciprocal Cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	 = 0.5
1/3	 = 0.(3)
1/4	 = 0.25
1/5	 = 0.2
1/6	 = 0.1(6)
1/7	 = 0.(142857)
1/8	 = 0.125
1/9	 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time

def recurring_cycle_length(denominator):
    digits = {0: 0}
    digit = 1
    decimal = 1
    while digit not in digits:
        digits[digit] = decimal
        decimal += 1
        dividend = digit * 10
        quotient = int(dividend / denominator)
        digit = dividend - (quotient * denominator)
    if digit == 0:
        return 0
    return decimal - digits[digit]

def longest_reciprocal_cycles(maximum):
    cycle_lengths = [0] * maximum
    for denominator in range(2, maximum):
        cycle_lengths[denominator] = recurring_cycle_length(denominator)
    longest_cycle = 0
    longest_cycle_denominator = 0
    for denominator, length in enumerate(cycle_lengths):
        longest_cycle = max(longest_cycle, length)
        if longest_cycle == length:
            longest_cycle_denominator = denominator
    return longest_cycle_denominator

answer = partial(longest_reciprocal_cycles, maximum = 1000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
