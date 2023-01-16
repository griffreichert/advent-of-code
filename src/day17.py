import numpy as np
from collections import defaultdict
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

# lcm = lcm(12,20)

with open('../data/day17.txt') as f:
    blasts = f.read().strip().split('\n')[0]

blasts = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
# B = len(blasts)
# print(B)


# from the point 0,0 representing the bottom left corner of each rock, create the rock by following these moves
rocks_list = [
    [(0, 0), (0, 1), (0, 2), (0,3)], 
    [(0, 1), (-1, 0),  (-1, 1), (-1, 2), (-2, 1)], 
    [(0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2)], 
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)], 
    [(0, 0), (0, 1), (-1, 0), (-1, 1)], 
]

print('expected repeat iter')
print(lcm(len(blasts), len(rocks_list)))

global chamber
chamber = defaultdict(int)

def move_coords(old_coords, dir='v'):
    """Take the coordinates of a falling rock and try to move it in a certain direction

    Parameters:
    - old_coords: list of tuples representing the (row, col) positions of rock
    - dir: defaults to down 'v', could be '<' to move left or '>' to move right

    Returns:
    - final coordinates of the rock
    - blocked: boolean
        - true if the old coordinates are blocked from moving in the direction
        - false if the rock can move 
    """
    dir_map = {
        '<': (0, -1),
        '>': (0, 1),
        'v': (-1, 0),
    }
    dy, dx = dir_map[dir]
    new_coords = [(cy + dy, cx + dx) for cy, cx in old_coords]
    # check that you havent moved out of bounds
    if all(cy >= 0 and 0 <= cx < 7 for cy, cx in new_coords):
        # check that none of the positions are occupied by a rock
        # if all(chamber[(cy, cx)] != 2 if (cy, cx) in chamber else True for cy, cx in new_coords):
        if all((cy, cx) not in chamber for cy, cx in new_coords):
            return new_coords, False
    return old_coords, True


def drop_rocks(num_rocks=1000000000000):
    heights = [0 for _ in range(7)]
    max_height = max(heights)
    rock_count = 0
    states = {}

    while True:
        for blast_idx, blast in enumerate(blasts):
            rock_idx = blast_idx % 4
            rock = rocks_list[rock_idx]

            # get the state of the top of the rocks


            # check if you have seen this state before
            if tuple()

            # initialize the coordinates of each rock
            coords = [(ry + max_height + 3, rx + 2) for ry, rx in rock]
            
            # start drop process
            blocked = False
            while not blocked:
                # blast rock left or right based on blast index
                coords, _ = move_coords(coords, blast)
                # drop it down
                coords, blocked = move_coords(coords, 'v')
            # set chambr coordinates to rock
            for cy, cx in coords: chamber[(cy, cx)] = 1

            

    #     for rock_idx, rock in enumerate(rock_types):
    #         rock_count += 1
    #         row = (highest - 4)
    #         for c in coords:
    #             chamber[c] = 1
    #         blocked = False
    #         while not blocked:

    #         # reset the old position to air
    #         chamber = np.where(chamber==1, 0, chamber)
    #         # turn falling rock into stationary rock 
    #         for c in coords:
    #             chamber[c] = 2
            
    #         # update highest point
    #         row_sum = np.sum(chamber, axis=1)
    #         highest = len(row_sum[np.where(row_sum == 0)])
            
    #         # represent the top of the pile of rocks as a tuple of 7 ints
    #         t = tuple(np.argmax(chamber, axis=0))
    #         t2 = tuple(n-i for i in t)
    #         t3 = tuple(i - min(t2) for i in t2)
    #         print(t)
    #         print(t2)
    #         print(t3)
    #         # show(chamber[:-10])
    #         return
    #         if rock_count % 1000 == 0:
    #             print(f'r: {rock_count}')

    #         if rock_count == num_rocks:
    #             break
    # # show(chamber)
    # return n - highest, chamber

# 1514285714288
# 1625000000000

def show(chamber):
    print()
    for row in chamber:
        print(' '.join(['.' if c == 0 else '#' if c == 2 else '@' for c in row]))
    print()    

# drop_rocks(200)

# v = chamber.shape[0] - height
# show(chamber[v-5:v+5])
# print([0])
# print(drop_a_lot_of_rocks())
# height, chamber = drop_rocks(2022)
# show(chamber[-10:])


# 1514285714288
# 76675000000000










# def move_coords(chamber, old_coords, dir='v'):
#     # dir can be <, >, v
#     if dir == '<':
#         dy, dx = 0, -1
#     elif dir == '>':
#         dy, dx = 0, 1
#     else:
#         dy, dx = 1, 0
        
#     new_coords = [(c[0] + dy, c[1] + dx) for c in old_coords]
#     # check that you havent hit a wall
#     if all([c[0] < chamber.shape[0] and 0 <= c[1] < 7 for c in new_coords]): 
#         if all([chamber[c] != 2 for c in new_coords]):
#             return new_coords, False
#     return old_coords, True


# def drop_rocks(num_rocks=1000000000000):
#     n = 3*(num_rocks+2)
#     chamber = np.zeros((n, 7), np.int8)
#     highest = n
#     rock_count = 0
#     blast_index = 0
#     states = {}
#     while rock_count < num_rocks:
#         for rock_idx, rock in enumerate(rock_types):
#             rock_count += 1
#             row = (highest - 4)
#             # initialize the coordinates of each rock
#             coords = [(p[0] + row, p[1] + 2) for p in rock]
#             for c in coords:
#                 chamber[c] = 1
#             # start drop process
#             blocked = False
#             while not blocked:
#                 # blast rock left or right based on blast index
#                 blast_char = blasts[blast_index % B]
#                 coords, _ = move_coords(chamber, coords, blast_char)
#                 blast_index += 1
#                 # drop it down
#                 coords, blocked = move_coords(chamber, coords, 'v')
#             # reset the old position to air
#             chamber = np.where(chamber==1, 0, chamber)
#             # turn falling rock into stationary rock 
#             for c in coords:
#                 chamber[c] = 2
            
#             # update highest point
#             row_sum = np.sum(chamber, axis=1)
#             highest = len(row_sum[np.where(row_sum == 0)])
            
#             # represent the top of the pile of rocks as a tuple of 7 ints
#             t = tuple(np.argmax(chamber, axis=0))
#             t2 = tuple(n-i for i in t)
#             t3 = tuple(i - min(t2) for i in t2)
#             print(t)
#             print(t2)
#             print(t3)
#             # show(chamber[:-10])
#             return
#             if rock_count % 1000 == 0:
#                 print(f'r: {rock_count}')

#             if rock_count == num_rocks:
#                 break
#     # show(chamber)
#     return n - highest, chamber 

# # def drop_a_lot_of_rocks():
# #     rocks_repeat = lcm(B, 5)
# #     print(rocks_repeat)
# #     repeat_height, base_chamber = drop_rocks(rocks_repeat)
# #     show(base_chamber[-10:])
# #     v = base_chamber.shape[0] - repeat_height
# #     show(base_chamber[v-5:v+5])

# #     gap = 0

# #     N = 1000000000000
# #     remainder = N % rocks_repeat
# #     full = N // rocks_repeat
    
# #     print(f'repeat_height: {repeat_height}')
# #     print(f'full: {full}')
# #     print(f'rem: {remainder}')
# #     bonus = drop_rocks(remainder)[0]
# #     print(f'bonus: {bonus}')

# #     return repeat_height + (full - 1) * (repeat_height - gap) + bonus


# # 1514285714288
# # 1625000000000

# def show(chamber):
#     print()
#     for row in chamber:
#         print(' '.join(['.' if c == 0 else '#' if c == 2 else '@' for c in row]))
#     print()    

# drop_rocks(200)

# # v = chamber.shape[0] - height
# # show(chamber[v-5:v+5])
# # print([0])
# # print(drop_a_lot_of_rocks())
# # height, chamber = drop_rocks(2022)
# # show(chamber[-10:])


# # 1514285714288
# # 76675000000000