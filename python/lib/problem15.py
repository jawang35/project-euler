# coding=utf-8
'''
Problem 15 - Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

from functools import partial
from lib.helpers.runtime import print_answer_and_elapsed_time


class GridRouteTracker:
    def __init__(self):
        self.grids = {}

    def parse_key(self, key):
        x, y = key[0], key[1]
        return (x, y) if x < y else (y, x)

    def __getitem__(self, key):
        return (1
                if key[0] == 0 or key[1] == 0
                else self.grids[self.parse_key(key)])

    def __setitem__(self, key, routes):
        self.grids[self.parse_key(key)] = routes


def lattice_paths(width, height):
    grid_route_tracker = GridRouteTracker()
    for x in range(1, width + 1):
        for y in range(1, max(x, width + 1)):
            routes = (grid_route_tracker[(x - 1, y)] +
                      grid_route_tracker[(x, y - 1)])
            grid_route_tracker[(x, y)] = routes
    return grid_route_tracker[(width, height)]

answer = partial(lattice_paths, width=20, height=20)

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
