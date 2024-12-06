from collections import Counter

import numpy as np
import utils

lines = utils.read_lines(__file__, parse_ints=False)
mapping = {
    "X": 0,
    "M": 1,
    "A": 2,
    "S": 3,
}


def is_xmas(grid, pos, dir, target=3) -> bool:
    letter = 0
    while True:
        npos = utils.update_pos_safe(pos, dir, grid.shape)
        if npos is not None:
            if grid[npos] == letter + 1:
                pos = npos
                letter += 1
                if letter == target:
                    return True
            else:
                break
        else:
            break
    return False


def p1():
    grid = np.array([[mapping[c] for c in line] for line in lines])
    x_pos = list((int(a), int(b)) for a, b in zip(*np.where(grid == 0)))
    return sum(is_xmas(grid, start, dir) for start in x_pos for dir in utils.neighbors)


def p2():
    grid = np.array([[mapping[c] for c in line] for line in lines]) - 1
    # utils.show_grid(grid, map={-1: ".", 0: "M", 1: "A", 2: "S"})
    m_pos = list((int(a), int(b)) for a, b in zip(*np.where(grid == 0)))
    mas_intersect_list = [
        utils.add_tuples(start, dir)
        for start in m_pos
        for dir in utils.diagonals
        if is_xmas(grid, start, dir, target=2)
    ]
    return sum(v == 2 for v in Counter(mas_intersect_list).values())


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
