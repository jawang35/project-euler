# Problem 1 - Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

from helpers import runtime

def multiples_of_3_and_5():
    number = 1000
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

runtime.print_answer_and_elapsed_time(multiples_of_3_and_5)
