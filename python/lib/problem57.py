# coding=utf-8
'''
Problem 57 - Square Root Convergents

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
'''

from lib.helpers.runtime import print_answer_and_elapsed_time


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return 'Fraction(%r/%r)' % (self.numerator, self.denominator)

    def __add__(self, other):
        denominator = self.denominator * other.denominator
        numerator = (self.numerator * other.denominator) + \
                    (other.numerator * self.denominator)
        return Fraction(numerator, denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


def square_root_fractions(iterations):
    fraction = Fraction(0, 1)

    for _ in range(iterations):
        fraction = (Fraction(2, 1) + fraction).inverse()
        yield Fraction(1, 1) + fraction


def answer():
    return len([f
                for f in square_root_fractions(1000)
                if len(str(f.numerator)) > len(str(f.denominator))])

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
