'''
Problem 41 - Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import sieve_of_eratosthenes

def largest_pandigital_prime():
    maximum = 7654321 # 8- and 9-digit primes are divisible by 3
    sieve = sieve_of_eratosthenes(maximum)
    for number, is_prime in reversed(list(enumerate(sieve))):
        if is_prime:
            number_string = ''.join(sorted(str(number)))
            number_length = len(number_string)
            if ''.join(sorted(str(number))) == '1234567'[:number_length]:
                return number

answer = largest_pandigital_prime

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
