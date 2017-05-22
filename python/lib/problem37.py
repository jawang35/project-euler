'''
Problem 37 - Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from lib.helpers.runtime import print_answer_and_elapsed_time
from lib.helpers.numbers import is_prime


def is_truncatable_prime(number):
    if not is_prime(number):
        return False

    number_string = str(number)
    number_length = len(number_string)

    if number_length < 2:
        return False

    for i in range(1, number_length):
        if (not is_prime(int(number_string[i:])) or
                not is_prime(int(number_string[:i]))):
            return False
    return True


def truncatable_primes():
    number = 11
    result = []
    while len(result) < 11:
        if is_truncatable_prime(number):
            result.append(number)
        number += 2
    return result


def answer():
    return sum(truncatable_primes())

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
