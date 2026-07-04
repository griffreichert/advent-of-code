from collections import defaultdict

import utils

lines = utils.read_lines(__file__, parse_ints=False)
# todo utils.mapchars

pipe_chars = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    # ".": [],
    # "S": what to do about the starting point,
}


def get_origin(tup):
    # if a tube send you to the right, that means you came in with a left
    return tuple(-1 * e for e in tup)


lines = [[char for char in line] for line in lines]
maze = defaultdict(list)
start = (0, 0)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char in pipe_chars:
            maze[(i, j)] = pipe_chars[char]
        elif char == "S":
            start = (i, j)

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
