import math
from functools import reduce
from itertools import combinations
from operator import mul

def sieve_of_eratosthenes(max):
    sieve = [True] * max
    sieve[0] = False
    sieve[1] = False
    for n in range(2, max):
        if sieve[n]:
            for m in range(2 * n, max, n):
                sieve[m] = False
    return sieve

def is_prime(number):
    sqrt_of_number = math.floor(math.sqrt(number)) + 1
    for n in range(2, sqrt_of_number):
        if number % n == 0:
            return False
    return True

def prime_divisors(number):
    sqrt_of_number = math.floor(math.sqrt(number)) + 1
    for n in range(2, sqrt_of_number):
        if number % n == 0:
            return prime_divisors(n) + prime_divisors(int(number / n))
    return [number]

def divisors(number):
    result = set()
    prime_divisors_list = prime_divisors(number)
    for n in range(1, len(prime_divisors_list) + 1):
        for combination in combinations(prime_divisors_list, n):
            result.add(reduce(mul, combination, 1))
    return result
