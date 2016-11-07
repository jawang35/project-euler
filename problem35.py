'''
Problem 35 - Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import sieve_of_eratosthenes

def circular_primes(maximum):
    sieve = sieve_of_eratosthenes(maximum)
    result = set([2])
    for number in range(3, maximum, 2):
        if not sieve[number] or number in result:
            continue
        number_string = str(number)
        rotations = [int(number_string[i:] + number_string[:i])
                     for i in range(len(number_string))]
        if len([p for p in rotations if sieve[p]]) == len(rotations):
            for prime in [p for p in rotations if p < maximum]:
                result.add(prime)
    return result

def answer():
    return len(circular_primes(1000000))

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
