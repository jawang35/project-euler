'''
Problem 50 - Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
'''

from lib.helpers.numbers import sieve_of_eratosthenes
from lib.helpers.runtime import print_answer_and_elapsed_time


def most_consecutive_prime_sum(maximum):
    primes = sieve_of_eratosthenes(maximum)
    prime_list = list(primes)
    prime_set = set(primes)
    number_of_primes_in_sum = result_sum_prime = total = 0

    for (starting_index, starting_prime) in enumerate(prime_list):
        next_prime_index = starting_index + number_of_primes_in_sum
        total = sum(prime_list[starting_index:next_prime_index])

        if total > maximum:
            break

        for (index, prime) in list(enumerate(prime_list))[next_prime_index:]:
            if total > maximum:
                break

            if total in prime_set:
                result_sum_prime = total
                number_of_primes_in_sum = index - starting_index

            total += prime

    return result_sum_prime


def answer():
    return most_consecutive_prime_sum(1000000)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
