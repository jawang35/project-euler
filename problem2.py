'''
Problem 2 - Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting
with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
the sum of the even-valued terms.
'''

from functools import partial
from helpers import runtime

def even_fibonacci_numbers(maximum):
    n1 = 1
    n2 = 1
    sum = 0
    while (n2 <= maximum):
        if n2 % 2 == 0:
            sum += n2
        n1, n2 = n2, n1 + n2
    return sum

runtime.print_answer_and_elapsed_time(partial(even_fibonacci_numbers, maximum = 4000000))
