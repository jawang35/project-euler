# coding=utf-8
'''
Problem 22 - Name Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

from lib.config import assets_path
from lib.helpers.runtime import print_answer_and_elapsed_time


def name_score(name):
    offset = (ord('A') - 1) * len(name)
    ascii_score = sum([ord(char) for char in list(name)])
    return ascii_score - offset


def total_name_scores(names):
    return sum([(i + 1) * name_score(name) for (i, name) in enumerate(names)])


def answer():
    with open('%s/problem22/names.txt' % assets_path) as file:
        names = sorted(file.read().replace('"', '').split(','))
        return total_name_scores(names)


if __name__ == '__main__':
        print_answer_and_elapsed_time(answer)
