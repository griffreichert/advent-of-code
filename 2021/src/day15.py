import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint

lines = utils.read_list(__file__, as_str=True)
grid = utils.lines_to_grid(lines)


def shortest_path(grid):
    n, m = grid.shape

    # dijkstras shortest path algorithm
    visited = np.zeros_like(grid, dtype="int")

    # initialise heap
    heap = [(0, (0, 0), [(0, 0)])]

    while True:
        cost, pos, path = heappop(heap)

        # if you have already visited this cell, skip as there is a shorter path to get to it already in the heap
        if visited[pos] == 1:
            continue

        # mark current cell as visited
        visited[pos] = 1

        # return the cost when you reach the end
        if pos == (n - 1, m - 1):
            return cost

        # add adjacent cells to the stack if not greater than cur + 1, within bounds
        for adj in utils.adjacents:
            ni, nj = utils.add_tuples(pos, adj)
            if 0 <= ni < n and 0 <= nj < m:
                heappush(heap, (cost + grid[ni, nj], (ni, nj), path + [(ni, nj)]))


expanded_grid = np.concatenate([grid + i for i in range(5)], axis=0)
expanded_grid = np.concatenate([expanded_grid + i for i in range(5)], axis=1)
expanded_grid = np.where(expanded_grid > 9, expanded_grid - 9, expanded_grid)

_p1 = shortest_path(grid)
_p2 = shortest_path(expanded_grid)

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
