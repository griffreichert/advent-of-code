from collections import Counter

import utils

lines = utils.read_lines(__file__, parse_ints=True)
# grid = utils.lines_to_grid(lines)


def p1():
    res = 0
    left = []
    right = []
    for l, r in lines:
        left.append(l)
        right.append(r)
    for l, r in zip(sorted(left), sorted(right)):
        res += abs(l - r)
    return res


def p2():
    res = 0

    left = []
    right = []
    for l, r in lines:
        left.append(l)
        right.append(r)

    rc = Counter(right)

    res = sum(rc[l] * l for l in left)

    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
