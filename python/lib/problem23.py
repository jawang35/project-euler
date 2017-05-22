'''
Problem 23 - Non-abundant Sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''

from lib.helpers.runtime import print_answer_and_elapsed_time
from lib.helpers.numbers import divisors


def is_abundant(number):
    return sum([n for n in divisors(number) if n < number]) > number


def sum_nonabundant_sums():
    maximum = 28123
    abundant_numbers = frozenset([n
                                  for n in range(maximum)
                                  if is_abundant(n)])
    abundant_sums = frozenset([x + y
                               for x in abundant_numbers
                               for y in abundant_numbers])
    return sum([n for n in range(maximum) if n not in abundant_sums])

answer = sum_nonabundant_sums

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
