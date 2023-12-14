import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint
import itertools
import math


lines = utils.read_lines(__file__, parse_ints=False)
# todo utils.mapchars

pipe_chars = {
    '': 
}

lines = [[char for char in line] for line in lines]
# grid = utils.lines_to_grid(lines)


# uitls.adjacents

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
def p1():
    res = 0
    return res


def p2():
    res = 0
    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
