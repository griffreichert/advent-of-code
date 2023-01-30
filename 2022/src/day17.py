from collections import defaultdict

with open('../data/day17.txt') as f:
    blasts = f.read().strip().split('\n')[0]
    
# blasts = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
B = len(blasts)

# from the point 0,0 representing the bottom left corner of each rock, create the rock by following these moves
rocks_list = [
    [(0, 0), (0, 1), (0, 2), (0,3)], 
    [(0, 1), (1, 0),  (1, 1), (1, 2), (2, 1)], 
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 
    [(0, 0), (1, 0), (2, 0), (3, 0)], 
    [(0, 0), (0, 1), (1, 0), (1, 1)], 
]

# use a defaultdict to store the coordinates of rocks, {(row,col): 1} when rock
global chamber
chamber = defaultdict(int)

def show(num_rows, tmp_coords=[]):
    print()
    for i in reversed(range(num_rows)):
        for j in range(7):
            c = '.'
            if (i, j) in tmp_coords:
                c = '%'
            elif (i, j) in chamber:
                c = '#'
            print(c, end=' ')
        print()
    print()

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
    if all(0 <= cy and 0 <= cx < 7 for cy, cx in new_coords):
        # check that none of the positions are occupied by a rock
        if all((cy, cx) not in chamber for cy, cx in new_coords):
            return new_coords, False
    return old_coords, True

def drop_rocks(num_rocks=1000000000000):
    heights = [-1 for _ in range(7)]
    max_height = max(heights)
    rock_count, blast_idx, repeat_height = 0, 0, 0
    # initialise dictionary to hold the states of the stack 
    states = {}

    while True:
        for rock_idx, rock in enumerate(rocks_list):
            # initialize the coordinates of each rock
            coords = [(ry + max_height + 4, rx + 2) for ry, rx in rock]
            # start drop process
            blocked = False
            while not blocked:
                # blast rock left or right based on blast index
                coords, _ = move_coords(coords, blasts[blast_idx])
                # increment blast index but keep it within the length of the string
                blast_idx = (blast_idx + 1) % B
                # drop it down
                coords, blocked = move_coords(coords, 'v')
            for cy, cx in coords: 
                # set chambr coordinates to rock
                chamber[(cy, cx)] = 1
                # update max height of each column
                heights[cx] = max(heights[cx], cy)
            # now that rock is locked in, increase the count of rocks dropped
            rock_count +=1 

            # get highest point
            max_height = max(heights)
            # scale heights so that the highest is 0, and others show distance below highest
            heights_tuple = tuple(h - max_height for h in heights)
            
            # get the state of the top of the rocks (you will be dropping the next rock so increment rock_idx)
            state_tuple = (heights_tuple, rock_idx + 1, blast_idx)
    
            # check if you have seen this state before
            if state_tuple in states:
                # get the height of the rocks and the number of rocks in the tower the last time you were at this state
                base_height, base_rock_count = states[state_tuple]
                
                ## A tower of rocks has three chunks
                # {remainder}
                # {repeat height}
                # {base height}
                # --------------
                        
                # find the number of rocks since the last time you were at this state
                # repeating this number of rocks will put you in the same position
                repeat_rock_count = rock_count - base_rock_count
                # find the number of times that many rocks repeats by floor dividing the 
                # number of rocks left to drop by the number of rocks in each repetition
                repeat = (num_rocks - rock_count) // repeat_rock_count
                # increment the rock count to jump to the end of the repeat height
                rock_count += repeat_rock_count * repeat
                # calculate the heigh of the total number of repeated sections
                repeat_height = repeat * (max_height - base_height)
                # reset states to avoid counting other repeats
                states = {}
                # continue looping to finish doing the remainder
            states[state_tuple] = max_height, rock_count
            
            # end looping condition: have you dropped the total number of rocks?
            if rock_count == num_rocks:
                res = max_height + repeat_height + 1
                print(res)
                return res
            
print('\nPart 1')
drop_rocks(2022)
chamber.clear()
print('\nPart 2')
drop_rocks(1000000000000)
print()