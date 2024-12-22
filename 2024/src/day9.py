import itertools
import math
import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from pprint import pprint

import numpy as np
import utils

disk = utils.read_lines(__file__, parse_ints=False)[0]
disk = [int(c) for c in disk]
# lines = utils.read_lines(__file__, parse_ints=True)
# grid = utils.lines_to_grid(lines)
# print(disk)


def p1():
    files = []
    pos = 0
    for i in range(0, len(disk), 2):
        file_size = disk[i]
        files.append((pos, pos + file_size))
        pos += file_size
        if i + 1 < len(disk):
            empty_space = disk[i + 1]
            pos += empty_space

    new_disk: list = [None] * files[-1][1]
    for k, rng in enumerate(files):
        start, end = rng
        for i in range(start, end):
            new_disk[i] = k

    i = 0
    while i < len(new_disk):
        while new_disk[-1] is None:
            new_disk.pop()
        if new_disk[i] is None:
            new_disk[i] = new_disk.pop()
        i += 1

    checksum = sum(i * k for i, k in enumerate(new_disk))
    return checksum


def p2():
    files = []
    empty_spaces = []
    pos = 0
    for i in range(0, len(disk), 2):
        file_size = disk[i]
        files.append((pos, pos + file_size))
        pos += file_size
        if i + 1 < len(disk):
            empty_space = disk[i + 1]
            empty_spaces.append((empty_space, (pos, pos + empty_space)))
            pos += empty_space

    files = {i: rng for i, rng in enumerate(files)}
    for i, (start, end) in reversed(files.items()):
        size = end - start
        for e in range(len(empty_spaces)):
            space, (space_start, space_end) = empty_spaces[e]
            if size <= space:
                files[i] = (space_start, space_start + size)
                new_space = (space_start + size, space_end)
                empty_spaces[e] = (space - size, new_space)
                break

    new_disk: list = [None] * max(max(tup) for tup in files.values())
    for k, rng in files.items():
        start, end = rng
        for i in range(start, end):
            new_disk[i] = k
    print(new_disk)
    checksum = sum(i * k if k is not None else 0 for i, k in enumerate(new_disk))

    # checksum = 0
    # for i, rng in files.items():
    #     a, b = rng
    #     for j in range(a, b):
    #         checksum += i * j
    return checksum


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
