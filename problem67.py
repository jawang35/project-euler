'''
Problem 67 - Maximum Path Sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the
maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...')
, a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to
solve this problem, as there are 2**99 altogether! If you could check one trillion (10**12) routes
every second it would take over twenty billion years to check them all. There is an efficient
algorithm to solve it. ;o)
'''

from functools import partial
from helpers import runtime
from problem18 import maximum_path_sum

if __name__ == '__main__':
    with open('assets/problem67/triangle.txt') as file:
        parse = lambda row: [int(n) for n in row.split(' ')]
        triangle = [parse(row) for row in file]
        runtime.print_answer_and_elapsed_time(partial(maximum_path_sum, triangle))
