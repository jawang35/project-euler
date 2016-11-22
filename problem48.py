'''
Problem 48 - Self Powers

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

from helpers.runtime import print_answer_and_elapsed_time

def self_powers_series(maximum):
    return sum([n ** n for n in range(1, maximum + 1)])

def answer():
    return str(self_powers_series(1000))[-10:]

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
