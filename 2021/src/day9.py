from collections import deque
import utils
import numpy as np
from pprint import pprint

lines = utils.read_list(__file__, as_str=True)
grid = utils.lines_to_grid(lines)
n, m = grid.shape


def p1():
    res = 0
    for i in range(n):
        for j in range(m):
            neighbors_lower_than = 0
            valid_neighbors = 0
            for adj in utils.adjacents:
                ni, nj = utils.add_tuples((i, j), adj)
                if 0 <= ni < n and 0 <= nj < m:
                    valid_neighbors += 1
                    if grid[i, j] < grid[ni, nj]:
                        neighbors_lower_than += 1
            if neighbors_lower_than == valid_neighbors:
                res += grid[i, j] + 1
    return res


def p2():
    # make a grid of where the peaks are (grid is 9)
    peaks = np.zeros_like(grid)
    peaks[np.where(grid == 9)] = 1

    # set of points we've seen
    seen = set()

    # list of basin sizes
    basins = []

    all_positions = deque([(i, j) for i in range(n) for j in range(m)])

    while all_positions:
        pos = all_positions.popleft()
        # if this position is already in a basin skip
        if pos in seen:
            continue
        # if we have hit a new peak, add it to seen and move on
        if peaks[pos]:
            seen.add(pos)
            continue

        # otherwise dfs for the basin
        basin = []
        basin_queue = deque([pos])
        while basin_queue:
            b_pos = basin_queue.popleft()
            # if this position is already in a basin skip
            if b_pos in seen:
                continue
            # if we have hit a new peak, add it to seen and move on
            if peaks[b_pos]:
                seen.add(b_pos)
                continue
            # add to the current basin
            basin.append(b_pos)
            seen.add(b_pos)
            for ni, nj in [utils.add_tuples(b_pos, adj) for adj in utils.adjacents]:
                if 0 <= ni < n and 0 <= nj < m:
                    # only append valid next points
                    basin_queue.append((ni, nj))
        # add the size of this basin to the overall list
        basins.append(len(basin))

    # find the 3 largest basins, multiply their sizes
    return utils.list_product(
        # find the three largest basins
        list(sorted(basins, reverse=True))[:3]
    )


print(f"p1{utils.Ansii.green}")
print(p1())
print(f"{utils.Ansii.clear}p2{utils.Ansii.green}")
print(p2())
