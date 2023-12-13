import utils
import numpy as np

lines = utils.read_lines(__file__, parse_ints=True)
lines = [tuple(utils.find_ints(line)) for line in lines]

n, m = 0, 0
for x1, y1, x2, y2 in lines:
    n = max(x1, x2, n)
    m = max(y1, y2, m)

grid = np.zeros((n + 1, m + 1), "int")


def p1(lines):
    for x1, y1, x2, y2 in lines:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        if x1 == x2:
            grid[min_y : max_y + 1, x1] += 1
        elif y1 == y2:
            grid[y1, min_x : max_x + 1] += 1
    return len(np.where(grid > 1)[0])


def p2(lines):
    for x1, y1, x2, y2 in lines:
        if x1 != x2 and y1 != y2:
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            diag = np.identity(max_x - min_x + 1, "int")
            if (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
                diag = diag[:, ::-1]
            grid[min_y : max_y + 1, min_x : max_x + 1] += diag
    return len(np.where(grid > 1)[0])


print("p1")
print(p1(lines))
print("p2")
print(p2(lines))
