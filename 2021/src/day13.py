import utils
import numpy as np

lines = utils.read_list(__file__, as_str=True)
# split points from fold instructions and parse inputs to correct dtypes
points = [tuple(line.split(",")) for line in lines[: lines.index("")]]
points = set((int(x), int(y)) for x, y in points)
folds = [tuple(line.split(" ")[-1].split("=")) for line in lines[lines.index("") + 1 :]]
# x for horizontal, y for vertical, b being the magnitude
folds = [(a, int(b)) for a, b in folds]

_p1 = None

for orientation, magnitude in folds:
    # set to hold new points after the fold
    new_points = set()
    # fold vertically (move your x coords)
    if orientation == "x":
        for x, y in points:
            if x > magnitude:
                x = magnitude - (x - magnitude)
            new_points.add((x, y))
    # fold horizontally (move your y cords)
    elif orientation == "y":
        for x, y in points:
            if y > magnitude:
                y = magnitude - (y - magnitude)
            new_points.add((x, y))
    points = new_points
    # count number of points after first fold for p1
    if not _p1:
        _p1 = len(points)


print(f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}")
# get dimensions for the grid
max_x, max_y = utils.tuple_max(points)
grid = np.zeros((max_y + 1, max_x + 1), dtype="int")
for x, y in points:
    grid[y, x] = 1
# print letters to screen
utils.show_grid(grid, map={0: " ", 1: "#"})
