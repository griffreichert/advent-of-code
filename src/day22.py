import numpy as np
from collections import defaultdict, Counter
import copy

with open('../data/day22.txt') as f:
    lines = f.read().strip().split('\n')

lines = """.....
..##.
..#..
.....
..##.
.....""".split('\n')

n, m = len(lines), len(lines[0])
# print(n, m)

grove = defaultdict(int)

for i in range(n):
    for j in range(m):
        if lines[i][j] == '#':
            grove[(i, j)] = 1

for elf in grove:
    print(elf)

def show(g):
    for i in range(n):
        for j in range(m): 
            print('#' if (i,j) in g else '.', end=' ')
        print()

def unstable_diffusion(g):
    """Move the elves around the grove based on the rules.
    
    Rules:
        During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

        - If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
        - If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
        - If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
        - If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

        After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.
    
    Method:
        Store current positions
        Record positions of where each elf wants to go to a dict of {(cur elf loc): (desired loc)}
        Create proposed grove with the count of elves that want to go to each position
        for each elf, if their proposed position is less than 1, move them there, otherwise they stay with the same location

    Returns:
    - new grove with elves in correct positions
    """
    
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1) 
    W = (0, -1)

    NE = (-1, 1)
    NW = (-1, -1)
    SE = (1, 1)
    SW = (1, -1)

    # Store current positions
    # default next position for each elf is thier current location
    pos_map = {elf: elf for elf in grove}

    # Record positions of where each elf wants to go to a dict of {(cur elf loc): (desired loc)}
    for elf in g:
        # if no elves in the 8 surrounding positions, the elf does not move
        surrounding = 0
        for n in [N, S, E, W, NE, NW, SE, SW]:
            t = tuple(x + y for x, y in zip(elf, n))
            # print(elf, n, t)
            if t in g:
                surrounding += 1
        if surrounding == 0:
            # print('skipping', elf)
            continue
        
        # try to move north
        if all([tuple(x + y for x, y in zip(elf, n)) not in g for n in [NW, N, NE]]):
            pos_map[elf] = tuple(x + y for x, y in zip(elf, N))
        # try to move south
        elif all([tuple(x + y for x, y in zip(elf, n)) not in g for n in [SW, S, SE]]):
            pos_map[elf] = tuple(x + y for x, y in zip(elf, S))
        # try to move west
        elif all([tuple(x + y for x, y in zip(elf, n)) not in g for n in [SW, W, NW]]):
            pos_map[elf] = tuple(x + y for x, y in zip(elf, W))
        # try to move east
        elif all([tuple(x + y for x, y in zip(elf, n)) not in g for n in [SE, E, NE]]):
            pos_map[elf] = tuple(x + y for x, y in zip(elf, E))
        # break
    # Create proposed grove with the count of elves that want to go to each position
    # for each elf, if their proposed position is less than 1, move them there, otherwise they stay with the same location
    print(pos_map)
    proposed = Counter(pos_map.values())
    
    print(proposed)
    final = defaultdict(int)
    for elf, dest in pos_map.items():
        if proposed[dest] < 2:
            final[dest] = 1
        else:
            final[elf] = 1
    return final

show(grove)
show(unstable_diffusion(grove))
"""
During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

- If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
- If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
- If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
- If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.
"""