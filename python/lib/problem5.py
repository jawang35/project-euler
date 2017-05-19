'''
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Computed by Hand:

Find prime factorizations of numbers from 2 to 20
2 = 2
3 = 3
4 = 2**2
5 = 5
6 = 2 * 3
7 = 7
8 = 2**3
9 = 3**2
10 = 2 * 5
11 = 11
12 = 2**2 * 3
13 = 13
14 = 2 * 7
15 = 3 * 5
16 = 2**4
17 = 17
18 = 2 * 3**2
19 = 19
20 = 2**2 * 5

Lowest common multiple is the product of the prime factors with the largest powers in the list above:
2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
'''

from lib.helpers.runtime import print_answer_and_elapsed_time

def answer():
    return 232792560

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
