import itertools
from collections import defaultdict

import utils

lines = utils.read_lines(__file__, parse_ints=False)
grid = [[c for c in line] for line in lines]
grid_shape = (len(grid), len(grid[0]))


def p1():
    def calculate_antinodes(a, b):
        unit = utils.sub_tuples(b, a)
        return utils.sub_tuples(a, unit), utils.add_tuples(unit, b)

    antennas = defaultdict(list)
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != ".":
                antennas[char].append((i, j))

    antinodes = set()
    for antenna_set in antennas.values():
        for a, b in itertools.combinations(antenna_set, 2):
            for antinode in calculate_antinodes(a, b):
                if utils.update_pos_safe(antinode, (0, 0), grid_shape) is not None:
                    antinodes.add(antinode)

    return len(antinodes)


def p2():
    def calculate_antinodes(a, b):
        unit = utils.sub_tuples(b, a)
        antinodes = []
        while True:
            a = utils.sub_tuples(a, unit)
            if utils.update_pos_safe(a, (0, 0), grid_shape) is None:
                break
            antinodes.append(a)
        while True:
            b = utils.add_tuples(unit, b)
            if utils.update_pos_safe(b, (0, 0), grid_shape) is None:
                break
            antinodes.append(b)
        return antinodes

    antennas = defaultdict(list)
    antinodes = set()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != ".":
                antennas[char].append((i, j))
                antinodes.add((i, j))

    for antenna_set in antennas.values():
        for a, b in itertools.combinations(antenna_set, 2):
            for antinode in calculate_antinodes(a, b):
                if utils.update_pos_safe(antinode, (0, 0), grid_shape) is not None:
                    antinodes.add(antinode)

    return len(antinodes)


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
