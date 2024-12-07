import itertools
import math
import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from pprint import pprint

import numpy as np
import utils
from tqdm import tqdm

# lines = utils.read_lines(__file__, parse_ints=False)
lines = utils.read_lines(__file__, parse_ints=False)


def p1():
    grid = np.array([[c for c in line] for line in lines])
    pos = list((int(a), int(b)) for a, b in zip(*np.where(grid == "^")))[0]
    dirs = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    dir = next(dirs)
    pos_seen = set()
    while True:
        pos_seen.add(pos)
        npos = utils.update_pos_safe(pos, dir, grid.shape)
        if npos is None:
            break
        if grid[npos] == "#":
            dir = next(dirs)
        else:
            pos = npos
    return len(pos_seen)


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def next_d(d):
    return (d + 1) % 4


def p2():
    grid = np.array([[c for c in line] for line in lines])
    pos = list((int(a), int(b)) for a, b in zip(*np.where(grid == "^")))[0]
    start = pos
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    pos_seen = set()
    while True:
        pos_seen.add(pos)
        npos = utils.update_pos_safe(pos, dirs[d], grid.shape)
        if npos is None:
            break
        if grid[npos] == "#":
            d = next_d(d)
        else:
            pos = npos

    def test_loop(block):
        # add a block at that position
        grid[block] = "#"
        pos = start
        d = 0
        seen = set()
        while True:
            if (pos, d) in seen:
                grid[block] = "."
                return True
            seen.add((pos, d))
            # go to next position based on current direction
            npos = utils.update_pos_safe(pos, dirs[d], grid.shape)
            # if we escape then no loop
            if npos is None:
                grid[block] = "."
                return False
            # if we hit a block, then turn
            if grid[npos] == "#":
                d = next_d(d)
                continue
            # update to the new position
            pos = npos

    return sum(test_loop(block) for block in pos_seen)


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
