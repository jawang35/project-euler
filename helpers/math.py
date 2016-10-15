import math

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
    sqrt_of_number = math.floor(math.sqrt(number))
    for n in range(2, sqrt_of_number + 1):
        if number % n == 0:
            return False
    return True
