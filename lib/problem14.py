#coding=utf-8
'''
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it
has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time

def longest_collatz_sequence(maximum):
    longest_sequence = 0
    result = 1
    sequence_lengths = {1:1}
    for number in range(2, maximum):
        n = number
        length = 0
        while n not in sequence_lengths:
            length += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
        length += sequence_lengths[n]
        sequence_lengths[number] = length
        if (length > longest_sequence):
            longest_sequence = length
            result = number
    return result

answer = partial(longest_collatz_sequence, maximum = 1000000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
