import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint


lines = utils.read_list(__file__, as_str=True)
grid = utils.lines_to_grid(lines)


def octopus_flashes(grid):
    n, m = grid.shape

    flash_counter = 0
    p1, p2 = None, None
    for step in range(1, 1_000):
        # increase all octopus by 1
        grid += 1

        # store the octopus that have flashed this round
        flashed = np.zeros_like(grid)

        # any new octopus with a value above 9 flashes
        while len(np.where((grid > 9) & (flashed == 0))[0]) > 0:
            # find the new octopus who have flashed
            flashing = np.where((grid > 9) & (flashed == 0))
            # increase all neighboring octopi by 1
            for pos in zip(flashing[0], flashing[1]):
                for adj in utils.neighbors:
                    ni, nj = utils.add_tuples(pos, adj)
                    if 0 <= ni < n and 0 <= nj < m:
                        grid[ni, nj] += 1
            # mark all octopus who have flashed in the round
            flashed[flashing] = 1

        # increment flash counter for the round
        step_flash = flashed.sum()
        flash_counter += step_flash

        # p1 criteria: number of flashes after 100 rounds
        if step == 100:
            p1 = flash_counter

        # p2 criteria: when all octopus flashed this round
        if step_flash == n * m:
            p2 = step

        # any octopus that flashed reset to 0
        grid[np.where(flashed == 1)] = 0

        # return p1, p2 tuple once we have both
        if p1 and p2:
            return p1, p2

    return None


_p1, _p2 = octopus_flashes(grid)

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
