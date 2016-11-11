'''
Problem 42 - Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and
adding these values we form a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
'''

from math import sqrt
from helpers.runtime import print_answer_and_elapsed_time

def is_triangle_number(number):
    n = int(sqrt(2 * number))
    return n * (n + 1) / 2 == number

def coded_number(word):
    offset = (ord('A') - 1) * len(word)
    ascii_sum = sum([ord(char) for char in list(word)])
    return ascii_sum - offset

def count_triangle_words(words):
    result = 0
    for word in words:
        if is_triangle_number(coded_number(word)):
            result += 1
    return result

def answer():
    with open('assets/problem42/words.txt') as file:
        words = sorted(file.read().replace('"', '').split(','))
        return count_triangle_words(words)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
