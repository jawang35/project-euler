from math import floor, sqrt
from functools import reduce
from itertools import combinations
from operator import mul


def sieve_of_eratosthenes(maximum):
    primes = set(range(2, maximum))
    for n in range(2, maximum):
        if n in primes:
            primes.difference_update(range(2 * n, maximum, n))
    return primes


def is_prime(number):
    if number < 2:
        return False
    sqrt_of_number = int(sqrt(number)) + 1
    for n in range(2, sqrt_of_number):
        if number % n == 0:
            return False
    return True


def prime_divisors(number):
    sqrt_of_number = int(sqrt(number)) + 1
    for n in range(2, sqrt_of_number):
        if number % n == 0:
            return prime_divisors(n) + prime_divisors(int(number / n))
    return [number]


def divisors(number):
    result = set([1])
    prime_divisors_list = prime_divisors(number)
    for n in range(1, len(prime_divisors_list) + 1):
        result.update([product(combination)
                       for combination in combinations(prime_divisors_list,
                                                       n)])
    return result


def product(numbers):
    return reduce(mul, numbers, 1)


def is_pentagonal(number):
    n = (1 + sqrt(1 - 4 * 3 * (-2) * number)) / 6
    return n.is_integer()


def is_triangular(number):
    n = int(sqrt(2 * number))
    return n * (n + 1) / 2 == number
