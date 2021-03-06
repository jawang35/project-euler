# coding=utf-8
'''
Problem 25 - 1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time


def fibonacci_number_of_size(digits):
    f1 = 1
    f2 = 1
    index = 2
    while len(str(f2)) < digits:
        f1, f2 = f2, f1 + f2
        index += 1
    return index

answer = partial(fibonacci_number_of_size, digits=1000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
