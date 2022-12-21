
from pprint import pprint

# with open('../data/day15.txt') as f:
with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')
    
    
def parse(line):
    sensor_str, beacon_str = line.split(':')
    s_i = eval(sensor_str.split('y=')[1].split(',')[0])
    s_j = eval(sensor_str.split('x=')[1].split(',')[0])
    b_i = eval(beacon_str.split('y=')[1].split(',')[0])
    b_j = eval(beacon_str.split('x=')[1].split(',')[0])
    return (s_i, s_j, b_i, b_j)

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
pprint(sensors)
print(min_i, max_i)
print(min_j, max_j)

num_rows = max_i-min_i+1
row_size = max_j-min_j+1
grid = [['.']*(row_size) for _ in range(num_rows)]

print(f'{len(grid), len(grid[0])}')

for s in sensors:
    print(s[1], s[3], min_j)
    grid[s[0]-min_i][s[1]-min_j] = 'S'
    grid[s[2]-min_i][s[3]-min_j] = 'B'

for row in grid:
    print(' '.join(row))