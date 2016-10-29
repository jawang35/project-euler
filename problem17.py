'''
Problem 17 - Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
numbers is in compliance with British usage.
'''

from functools import partial
from helpers.runtime import print_answer_and_elapsed_time

ones = {
    '1': 3, # one
    '2': 3, # two
    '3': 5, # three
    '4': 4, # four
    '5': 4, # five
    '6': 3, # six
    '7': 5, # seven
    '8': 5, # eight
    '9': 4, # nine
}

tens = {
    '1': 3, # ten
    '2': 6, # twenty
    '3': 6, # thirty
    '4': 5, # forty
    '5': 5, # fifty
    '6': 5, # sixty
    '7': 7, # seventy
    '8': 6, # eighty
    '9': 6, # ninety
}

teens = {
    '11': 6, # eleven
    '12': 6, # twelve
    '13': 8, # thirteen
    '14': 8, # fourteen
    '15': 7, # fifteen
    '16': 7, # sixteen
    '17': 9, # seventeen
    '18': 8, # eighteen
    '19': 8, # nineteen
}

def number_letter_counts(maximum):
    sum = 0
    for n in range(1, maximum + 1):
        copy = n
        if copy > 999:
            sum += ones[str(copy)[0]] + 8 # thousand
            copy = copy % 1000
        if copy > 99:
            sum += ones[str(copy)[0]] + 7 # hundred
            copy = copy % 100
        if n > 99 and copy > 0:
            sum += 3 # and
        if copy > 9:
            if copy > 19:
                sum += tens[str(copy)[0]]
                copy = copy % 10
            else:
                if copy > 10:
                    sum += teens[str(copy)]
                else:
                    sum += tens['1']
                copy = 0
        if copy > 0:
            sum += ones[str(copy)]
    return sum

if __name__ == '__main__':
    print_answer_and_elapsed_time(partial(number_letter_counts, maximum = 1000))
