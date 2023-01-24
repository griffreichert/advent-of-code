from collections import defaultdict
import sys

EXAMPLE = True if '-e' in sys.argv else False

# Example case: part 1 expects 6032 
inpt = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.""".split('\n')
moves = '10R5L5R10L4R5L5'

if not EXAMPLE:
    with open('../data/day22.txt', 'r') as fh:
        lines, moves = fh.read().strip("\n").split("\n\n")
        lines = lines.split('\n')
        
"""LOGIC FOR PART 2 (Example)
face map
        0       4       8      12
          -----------------
          |               v
0         |             # # #
          |       --->  # 3 #  <-----------
          |       |     # # #             |
          v       v     -----             |
4       # # # | # # # | # # #             |
   -->  # 1 # | # 2 # | # 4 #  <---       |
   |    # # # | # # # | # # #     |       |
   |      ^       ^     -----     v       |
8  |      |       |     # # # | # # #     |
   |      |       --->  # 5 # | # 6 #  <---
   |      |             # # # | # # #
   |      |               ^       ^
   |      -----------------       |
   --------------------------------
"""

face_map = {}   # keys: (row, column, facing), values: (new_row, new_column, new_facing)
for i in range(4):
    face_map[(4, i, 3)] = (0, 11 - i, 1) # 1 to 3 link
    face_map[(0, 11 - i, 3)] = (4, i, 1) # 3 to 1 link
    
    face_map[(7, i, 1)] = (11, 11 - i, 3) # 1 to 5 link
    face_map[(11, 11 - i, 1)] = (7, i, 3) # 5 to 1 link
    
    face_map[(4 + i, 0, 2)] = (11, 15 - i, 3) # 1 to 6 link
    face_map[(11, 15 - i, 1)] = (4 + i, 0, 0) # 6 to 1 link
    
    face_map[(4, 4 + i, 3)] = (i, 8, 0) # 2 to 3 link
    face_map[(i, 8, 2)] = (4, 4 + i, 1) # 3 to 2 link
    
    face_map[(7, 4 + i, 1)] = (11 - i, 8, 3) # 2 to 5 link
    face_map[(11 - i, 8, 1)] = (7, 4 + i, 3) # 5 to 2 link
    
    face_map[(i, 11, 0)] = (11 - i, 15, 2) # 3 to 6 link
    face_map[(11 - i, 15, 0)] = (i, 11, 2) # 6 to 3 link
    
    face_map[(4 + i, 11, 0)] = (8, 15 - i, 1) # 4 to 6 link
    face_map[(8, 15 - i, 3)] = (4 + i, 11, 2) # 6 to 4 link

OPEN_SPACE = 7
BLOCKED_SPACE = 8

arrow_nums = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3,
}

arrow_adj = {
    0: (0, 1),   # >
    1: (1, 0),   # v
    2: (0, -1),  # <
    3: (-1, 0),  # ^
}

print_grid = {
    OPEN_SPACE: ' ',
    BLOCKED_SPACE: '.',
    0: '>',
    1: 'v',
    2: '<',
    3: '^',
}

"""LOGIC FOR PART 2
face map
             .       .       .   .
             0      50     100   149
     ------------------|       |-------------- 
     |                 v       v             |
0    |               # # # | # # #           |
     |  ---------->  # 2 # | # 1 #  <-----   |
     |  |            # # # | # # #       |   |
     |  |            -----     ^         |   |
50   |  |            # # #     |         |   |
     |  |      --->  # 3 #  <---         |   |
     |  |      |     # # #               |   |
     |  |      v     -----               |   |
100  |  |    # # # | # # #               |   |
     |  -->  # 5 # | # 4 #  <-------------   |
     |       # # # | # # #                   |
     |       -----     ^                     |
150  |       # # #     |                     |
     ----->  # 6 #  <---                     |
             # # #                           |
               ^                             |
               |                             |
               -------------------------------
"""
if not EXAMPLE:
    face_map = {}   # keys: (row, column, facing), values: (new_row, new_column, new_facing)
    for i in range(50):
        face_map[(49, 100 + i, 1)] = (50 + i, 99, 2) # 1 to 3 link
        face_map[(50 + i, 99, 0)] = (49, 100 + i, 3) # 3 to 1 link

        face_map[(i, 149, 0)] = (149 - i, 99, 2) # 1 to 4 link
        face_map[(149 - i, 99, 0)] = (i, 149, 2) # 4 to 1 link

        face_map[(0, 100 + i, 3)] = (199, i, 3) # 1 to 6 link
        face_map[(199, i, 1)] = (0, 100 + i, 1) # 6 to 1 link

        face_map[(i, 50, 2)] = (100 + i, 0, 0) # 2 to 5 link
        face_map[(100 + i, 0, 2)] = (i, 50, 0) # 5 to 2 link

        face_map[(0, 50 + i, 3)] = (199 - i, 0, 0) # 2 to 6 link
        face_map[(199 - i, 0, 2)] = (0, 50 + i, 1) # 6 to 2 link

        face_map[(50 + i, 50, 2)] = (100, i, 1) # 3 to 5 link
        face_map[(100, i, 3)] = (50 + i, 50, 0) # 5 to 3 link

        face_map[(149, 50 + i, 1)] = (150 + i, 49, 2) # 4 to 6 link
        face_map[(150 + i, 49, 0)] = (149, 50 + i, 3) # 6 to 4 link


# default dict to store (row, col): value for value in print_grid
grid = defaultdict(int)

# number of rows and columns
n, m = len(lines), max(len(l) for l in lines)

def show(end=None):
    for i in range(n):
        for j in range(m):
            c = ' '
            if (i, j) in grid:
                c = print_grid[grid[(i, j)]]
            # if any((i, j, tmp_f) in face_map for tmp_f in range(4)):
            #     c = '!'
            if (i, j) == pos:
                c = '@'
            print(c, end=' ')
        print()
    print()

# fill in grid and row ranges
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '.':
            grid[(i, j)] = OPEN_SPACE
        elif c == '#':
            grid[(i, j)] = BLOCKED_SPACE

# Init starting position: (top left), facing: '>' = 0
pos = (0, min([k[1] for k in grid.keys() if k[0] == 0]))
f = 0

def update_facing(turn):
    global f
    if turn == 'R':
        f = (f + 1) % 4
    elif turn == 'L':
        f = (f - 1) % 4
    assert f in range(4)

def update_pos(cube=False):
    global pos, f   # reference global pos & f variables to update
    npos = (-1, -1)
    ni, nj = tuple(x + y for x, y in zip(pos, arrow_adj[f])) # move position 1 unit in the direction we are currently facing
    f_copy = f
    if cube:
        if (*pos, f) in face_map:
            ni, nj, f = face_map[(*pos, f)]
    else:
        # check that new position is in the grid
        if (ni, nj) not in grid:
            if f == 0: # >
                nj = min([k[1] for k in grid.keys() if k[0] == ni])
            elif f == 2: # <
                nj = max([k[1] for k in grid.keys() if k[0] == ni])
            elif f == 1: # v
                ni = min([k[0] for k in grid.keys() if k[1] == nj])
            elif f == 3: # ^
                ni = max([k[0] for k in grid.keys() if k[1] == nj])
            else:
                assert False
    npos = (ni, nj)
    # if the new space is blocked, dont update the position
    assert npos in grid, (pos, f_copy, npos, f)
    if npos in grid and grid[npos] == BLOCKED_SPACE:
        return False
    pos = npos
    grid[pos] = f
    return True
    
def trace_path(moves, cube=False):
    i = 0
    global pos
    while i < len(moves):
        grid[pos] = f   # mark current position with new way you are facing
        
        if moves[i].isnumeric():    # if you read a number, move that many steps
            j = i + 1
            while j < len(moves) and moves[j].isnumeric():
                j += 1
            steps = eval(moves[i:j])
            
            for _ in range(steps):
                if not update_pos(cube=cube):   # if you update position and are blocked, skip to the next instr
                    break
            i = j # jump forward in moves
        
        else:   # if your current position is not a number, it must be an L or an R
            assert moves[i] in 'LR', (i, moves[i])
            update_facing(moves[i])
            i += 1
    # if EXAMPLE: show()
    show()
    print('done @', pos)
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + grid[pos]
    
            
# def calc_password():
#     # The final password is the sum of 1000 times the row, 4 times the column, and the facing. (rows & cols start at 1)
#     global f
#     ci, cj = pos
#     print(ci + 1, cj + 1, grid[pos])
#     return 1000 * (ci + 1) + 4 * (cj + 1) + grid[(ci, cj)]

# pt1 = trace_path(moves)
# print('Part 1:', pt1)

# Reset for part 2
for k, v in grid.items():
    if v != BLOCKED_SPACE:
        grid[k] = OPEN_SPACE

# Init starting position: (top left), facing: '>' = 0
pos = (0, min([k[1] for k in grid.keys() if k[0] == 0]))
f = 0

# pt2 = trace_path(moves, cube=True)
# print('Part 2:', pt2)

# print('Expected:', 162038)


test_cases = [ # test pos, test f, expect pos, expect f
    ((49, 100), 1, (50, 99), 2),    # 1 to 3 link
    



    ((99, 99), 0, (49, 149), 3),    # 3 to 1 link
    ((1, 149), 0, (49, 149), 3),    # 1 to 4 link
    ((101, 99), 0, (48, 149), 2),   # 4 to 1 link
    ((101, 0), 3, ()),     # 1 to 6 link
    (),     # 6 to 1 link
    (),     # 2 to 5 link
    (),     # 5 to 2 link
    (),     # 2 to 6 link
    (),     # 6 to 2 link
    (),     # 3 to 5 link
    (),     # 5 to 3 link
]

for tpos, tf, epos, ef in test_cases:
    pos, f = tpos, tf
    if update_pos(cube=True): 
        assert (pos, f) == (epos, ef), (tpos, tf, pos, f)
    else:
        print('blocked:', pos)
        
# 1 to 3 link
# 3 to 1 link

# 1 to 4 link
# 4 to 1 link
    
# 1 to 6 link
# 6 to 1 link

# 2 to 5 link
# 5 to 2 link

# 2 to 6 link
# 6 to 2 link

# 3 to 5 link
# 5 to 3 link

# 4 to 6 link
# 6 to 4 link