import numpy as np
import math
from copy import deepcopy
from aoc_tools import *

with open('../data/day17.txt') as f:
    blasts = f.read().strip().split('\n')[0]

blasts = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
B = len(blasts)
print(B)


# from the point 0,0 representing the bottom left corner of each rock, create the rock by following these moves
rock_types = [
    [(0, 0), (0, 1), (0, 2), (0,3)], 
    [(0, 1), (-1, 0),  (-1, 1), (-1, 2), (-2, 1)], 
    [(0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2)], 
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)], 
    [(0, 0), (0, 1), (-1, 0), (-1, 1)], 
]

def move_coords(chamber, old_coords, dir='v'):
    # dir can be <, >, v
    if dir == '<':
        dy, dx = 0, -1
    elif dir == '>':
        dy, dx = 0, 1
    else:
        dy, dx = 1, 0
        
    new_coords = [(c[0] + dy, c[1] + dx) for c in old_coords]
    # check that you havent hit a wall
    if all([c[0] < chamber.shape[0] and 0 <= c[1] < 7 for c in new_coords]): 
        if all([chamber[c] != 2 for c in new_coords]):
            return new_coords, False
    return old_coords, True


def drop_rocks(num_rocks):
    n = 3*(num_rocks+2)
    chamber = np.zeros((n, 7), np.int8)
    highest = n
    rock_count = 0
    blast_index = 0
    while rock_count < num_rocks:
        for rock in rock_types:
            rock_count += 1
            row = (highest - 4)
            # initialize the coordinates of each rock
            coords = [(p[0] + row, p[1] + 2) for p in rock]
            for c in coords:
                chamber[c] = 1
            # start drop process
            blocked = False
            while not blocked:
                # blast it left or right based on blast index
                blast_char = blasts[blast_index % B]
                blast_index += 1
                # blast rock
                coords, _ = move_coords(chamber, coords, blast_char)
                # drop it down
                coords, blocked = move_coords(chamber, coords, 'v')
            # reset the old position to air
            chamber = np.where(chamber==1, 0, chamber)
            # turn falling rock into stationary rock 
            for c in coords:
                chamber[c] = 2
            
            # update highest point
            row_sum = np.sum(chamber, axis=1)
            highest = len(row_sum[np.where(row_sum == 0)])
            
            if rock_count % 1000 == 0:
                print(f'r: {rock_count}')

            if rock_count == num_rocks:
                break
    # viz(chamber)
    return n - highest, chamber 

def drop_a_lot_of_rocks():
    rocks_repeat = int(lcm(B, 5))
    print(rocks_repeat)
    repeat_height, base_chamber = drop_rocks(rocks_repeat)
    viz(base_chamber[-10:])
    v = base_chamber.shape[0] - repeat_height
    viz(base_chamber[v-5:v+5])

    gap = 0

    N = 1000000000000
    remainder = N % rocks_repeat
    full = N // rocks_repeat
    
    print(f'repeat_height: {repeat_height}')
    print(f'full: {full}')
    print(f'rem: {remainder}')
    bonus = drop_rocks(remainder)[0]
    print(f'bonus: {bonus}')

    return repeat_height + (full - 1) * (repeat_height - gap) + bonus


# 1514285714288
# 1625000000000

def viz(chamber):
    print()
    for row in chamber:
        print(' '.join(['.' if c == 0 else '#' if c == 2 else '@' for c in row]))
    print()    

# v = chamber.shape[0] - height
# viz(chamber[v-5:v+5])
# print([0])
print(drop_a_lot_of_rocks())
# height, chamber = drop_rocks(2022)
# viz(chamber[-10:])


1514285714288
76675000000000