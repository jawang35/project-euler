'''
Problem 43 - Sub-string Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0
to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from helpers.runtime import print_answer_and_elapsed_time

def prepended_multiples(right_two_digits, factors, digits):
    result = []
    for multiple in [d + right_two_digits for d in digits]:
        if int(multiple) % factors[-1] > 0:
            continue

        remaining_digits = digits - set([multiple[0]])
        if len(remaining_digits) == 1:
            result.append(list(remaining_digits)[0] + multiple)
            continue

        next_substring = prepended_multiples(multiple[:2], factors[:-1], remaining_digits)
        result.extend([substring + multiple[2] for substring in next_substring])
    return result

def substring_divisible_numbers():
    multiples_of_17 = range(17, 1000, 17)
    digits = set('1234567890')
    factors = [2, 3, 5, 7, 11, 13]
    result = []
    for multiple_of_17 in [('0' + str(n))[-3:] for n in multiples_of_17]:
        if len(set(multiple_of_17)) < len(multiple_of_17):
            continue
        left_substrings = prepended_multiples(multiple_of_17[:2], factors, digits - set(multiple_of_17))
        result.extend([left_substring + multiple_of_17[2] for left_substring in left_substrings])
    return result

def answer():
    return sum([int(number) for number in substring_divisible_numbers()])

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
