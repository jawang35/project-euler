#coding=utf-8
'''
Problem 39 - Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from functools import partial
from math import ceil
from helpers.runtime import print_answer_and_elapsed_time

def right_triangle_sides(perimeter):
    result = set()
    for a in range(1, ceil(perimeter / 3)):
        b = int((perimeter**2 - 2 * perimeter * a) / (2 * perimeter - 2 * a))
        c = perimeter - a - b
        if a**2 + b**2 == c**2:
            result.add((min(a, b), max(a, b), c))
    return result

def most_integer_right_triangles(maximum):
    result_perimeter = 0
    result_solutions = 0
    for perimeter in range(12, maximum):
        solutions = len(right_triangle_sides(perimeter))
        if solutions > result_solutions:
            result_perimeter = perimeter
            result_solutions = solutions
    return result_perimeter

answer = partial(most_integer_right_triangles, maximum = 1001)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
