#coding=utf-8
'''
Problem 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into
n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import divisors

def sum_of_proper_divisors(number):
    return sum([divisor for divisor in divisors(number) if divisor < number])

def sum_amicable_numbers(maximum):
    amicable_number_set = set()
    for n in range(maximum):
        if n not in amicable_number_set:
            m = sum_of_proper_divisors(n)
            if m != n and sum_of_proper_divisors(m) == n:
                amicable_number_set.add(n)
                amicable_number_set.add(m)
    return sum([number for number in amicable_number_set if number < maximum])

answer = partial(sum_amicable_numbers, maximum = 10000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
