import utils
import numpy as np

lines = utils.read_list(__file__, as_str=True)
lines = [tuple(utils.find_int(line, all=True)) for line in lines]

n, m = 0, 0
for x1, y1, x2, y2 in lines:
    n = max(x1, x2, n)
    m = max(y1, y2, m)

print(lines)
print(n, m)
def p1(lines):
    grid = np.zeros((n+1, m+1), 'int')
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            grid[min(y1, y2):max(y1, y2)+1, x1] += 1
        if y1 == y2:
            grid[y1, min(x1, x2):max(x1, x2)+1] += 1
    print(grid)
    return np.where(grid > 1)


def p2(lines):
    return -1

print("p1")
print(p1(lines))
print("p2")
print(p2(lines))
