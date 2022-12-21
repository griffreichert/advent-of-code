
from pprint import pprint
import numpy as np

with open('../data/day15.txt') as f:
# with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')
    
    
def parse(line):
    sensor_str, beacon_str = line.split(':')
    s_i = eval(sensor_str.split('y=')[1].split(',')[0])
    s_j = eval(sensor_str.split('x=')[1].split(',')[0])
    b_i = eval(beacon_str.split('y=')[1].split(',')[0])
    b_j = eval(beacon_str.split('x=')[1].split(',')[0])
    return (s_i, s_j, b_i, b_j)

def dist(s_i, s_j, b_i, b_j):
    return abs(s_i - b_i) + abs(s_j - b_j)

sensors = [parse(line) for line in lines]
min_i = 0
max_i = 0
min_j = 0
max_j = 0
for s in sensors:
    min_i = min(min_i, min(s[0], s[2]))
    max_i = max(max_i, max(s[0], s[2]))
    min_j = min(min_j, min(s[1], s[3]))
    max_j = max(max_j, max(s[1], s[3]))
# pprint(sensors)
# print(min_i, max_i)
# print(min_j, max_j)

num_rows = max_i-min_i+1
row_size = max_j-min_j+1
grid = np.zeros((num_rows, row_size), dtype='short')

print(f'{grid.shape}')

for s in sensors:
    s_i = s[0]-min_i
    s_j = s[1]-min_j
    b_i = s[2]-min_i
    b_j = s[3]-min_j
    
    d = dist(s_i, s_j, b_i, b_j)
    
    # draw rectangles
    for i in range(d+1):
        height = 2*(i) + 1
        width = 2*(d-i) + 1
        start_i = max(s_i - (i), 0)
        end_i = min(s_i - (i) +height, num_rows)
        start_j = max(s_j - (d-i), 0)
        end_j = min(s_j - (d-i)+width, row_size)
        grid[start_i:end_i, start_j:end_j] = 1
        # for w in range(width):
        #     for h in range(height):
        #         ii = start_i + h
        #         jj = start_j + w
        #         if (0 <= ii < num_rows) and (0 <= jj < row_size):
        #             if grid[ii,jj] == 5 or grid[ii][jj] == 8:
        #                 continue
        #             grid[ii][jj] = 1
    # break

for s in sensors:
    s_i = s[0]-min_i
    s_j = s[1]-min_j
    b_i = s[2]-min_i
    b_j = s[3]-min_j
    
    grid[s_i][s_j] = 5
    grid[b_i][b_j] = 8        
        
        
for row in grid:
    print(' '.join(['.' if i == 0 else '#' if i == 1 else 'S' if i == 5 else 'B' for i in row]))
print()
    
print()
print(len(np.where(grid[10] == 1)[0]))
# print(len(np.where(grid[2000000] == 1)[0]))
