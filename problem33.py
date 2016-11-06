'''
Problem 33 - Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from helpers.runtime import print_answer_and_elapsed_time
from helpers.numbers import prime_divisors, product

def simplify(numerator, denominator):
    numerator_divisors = prime_divisors(numerator)
    denominator_divisors = prime_divisors(denominator)
    simplified_numerator = numerator
    simplified_denominator = denominator
    for i, divisor in enumerate(numerator_divisors):
        if divisor in denominator_divisors:
            simplified_numerator /= divisor
            simplified_denominator /= divisor
    return int(simplified_numerator), int(simplified_denominator)

def cancel_digits(numerator, denominator):
    numerator_string = str(numerator)
    denominator_string = str(denominator)
    results = set()
    for i, digit in enumerate(numerator_string):
        j = denominator_string.find(digit)
        if j > -1:
            simplified_numerator = int(numerator_string[:i] + numerator_string[i + 1:])
            simplified_denominator = int(denominator_string[:j] + denominator_string[j + 1:])
            if simplified_numerator > 0 and simplified_denominator > 0:
                results.add((simplified_numerator, simplified_denominator))
    return results

def digit_cancelling_fractions(digits):
    minimum = 10**(digits - 1)
    maximum = (10**digits)
    result_fractions = []
    for denominator in range(minimum, maximum):
        for numerator in range(minimum, denominator):
            simplified_fractions = cancel_digits(numerator, denominator)
            for simplified_numerator, simplified_denominator in simplified_fractions:
                divisor = numerator / simplified_numerator
                if denominator / simplified_denominator == divisor and divisor % minimum > 0:
                    result_fractions.append((numerator, denominator))
                    break
    return result_fractions

def answer():
    fractions = digit_cancelling_fractions(2)
    numerator_product = product([numerator for numerator, _ in fractions])
    denominator_product = product([denominator for _, denominator in fractions])
    simplified_product = simplify(numerator_product, denominator_product)
    return simplified_product[1]

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
