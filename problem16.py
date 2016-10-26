'''
Problem 16 - Power Digit Sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

from functools import partial
from helpers import runtime

def double_number_string(number_string):
    carry = 0
    result_list = []
    for i in range(len(number_string)):
        char_index = -i - 1
        double_char = 2 * int(number_string[char_index]) + carry
        result_list.append(str(double_char % 10))
        carry = int(double_char / 10)
    if carry > 0:
        result_list.append(str(carry))
    return "".join(reversed(result_list))

def power_digit_sum(power):
    power_of_two = "1"
    for n in range(1, power + 1):
        power_of_two = double_number_string(power_of_two)
    return sum([int(digit) for digit in list(power_of_two)])

if __name__ == "__main__":
    runtime.print_answer_and_elapsed_time(partial(power_digit_sum, power = 1000))
