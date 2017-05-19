'''
Problem 36 - Double-base Palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time
from lib.helpers.strings import is_palindrome

def decimal_to_base(number, base):
    power = 0
    while base**power <= number:
        power += 1
    power -= 1
    number_string = ''
    for p in range(power, -1, -1):
        current_value = base**p
        if current_value <= number:
            number_string += '1'
            number -= current_value
        else:
            number_string += '0'
    return number_string

def sum_double_base_palindromes(maximum, other_base):
    return sum([number
                for number in range(maximum)
                if is_palindrome(str(number))
                and is_palindrome(decimal_to_base(number, other_base))])

answer = partial(sum_double_base_palindromes, maximum = 1000000, other_base = 2)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
