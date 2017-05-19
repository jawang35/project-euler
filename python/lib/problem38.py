#coding=utf-8
'''
Problem 38 - Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the
concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
of an integer with (1,2, ... , n) where n > 1?
'''

from lib.helpers.runtime import print_answer_and_elapsed_time

def concatenate_products(number):
    result_string = ''
    for n in range(1, 10):
        result_string += str(number * n)
        if len(result_string) >= 9:
            break
    return int(result_string)

def is_pandigital(number):
    return ''.join(sorted(str(number))) == '123456789'

def largest_pandigital_multiple():
    maximum = 9876
    result = 0
    for number in range(maximum):
        concatenated_product = concatenate_products(number)
        if concatenated_product > result and is_pandigital(concatenated_product):
            result = concatenated_product
    return result

answer = largest_pandigital_multiple

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
