import numpy as np
from copy import deepcopy

with open('../data/day17.txt') as f:
    blasts = f.read().strip().split('\n')[0]

# blasts = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
B = len(blasts)


# from the point 0,0 representing the bottom left corner of each rock, create the rock by following these moves
rock_types = [
    [(0, 0), (0, 1), (0, 2), (0,3)], 
    [(0, 1), (-1, 0),  (-1, 1), (-1, 2), (-2, 1)], 
    [(0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2)], 
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)], 
    [(0, 0), (0, 1), (-1, 0), (-1, 1)], 
]


def drop_rocks(num_rocks):
    n = 3*(num_rocks+2)
    chamber = np.zeros((n, 7), np.int8)
    high = n
    rock_count = 0
    blast_index = 0
    while rock_count < num_rocks:
        for rock in rock_types:
            rock_count += 1
            row = (high - 4)
            # initialize the coordinates of each rock
            coords = [(p[0] + row, p[1] + 2) for p in rock]
            for c in coords:
                chamber[c] = 1
            # start drop process
            while True:
                # blast it left or right based on blast index
                blast_char = blasts[blast_index % B]
                blast_index += 1
                # blast right
                if blast_char == '>':
                    new_coords = [(c[0], c[1] + 1) for c in coords]
                    # check that you havent hit a wall
                    if all([c[1] < 7 for c in new_coords]): 
                        if all([chamber[c] != 2 for c in new_coords]):
                            coords = deepcopy(new_coords)
                # blast left:
                elif blast_char == '<':
                    new_coords = [(c[0], c[1] - 1) for c in coords]
                    # check that you havent hit a wall
                    if all([c[1] >= 0 for c in new_coords]): 
                        if all([chamber[c] != 2 for c in new_coords]):
                            coords = deepcopy(new_coords)
                # drop it down
                new_coords = [(c[0] + 1, c[1]) for c in coords]
                # check that you havent hit the bottom
                if all([c[0] < n for c in new_coords]): 
                    if all([chamber[c] != 2 for c in new_coords]):
                        coords = deepcopy(new_coords) 
                    else:
                        break
                else:
                    break
            # reset the old position to air
            chamber = np.where(chamber==1, 0, chamber)
            # turn falling rock into stationary rock 
            for c in coords:
                chamber[c] = 2
            
            # update highest point
            row_sum = np.sum(chamber, axis=1)
            high = len(row_sum[np.where(row_sum == 0)])
                        
            if rock_count == num_rocks:
                break
    viz(chamber)
    return n - high
                
            
def viz(chamber):
    print()
    for row in chamber:
        print(' '.join(['.' if c == 0 else '#' if c == 2 else '@' for c in row]))
    print()    
    
print(drop_rocks(2022))