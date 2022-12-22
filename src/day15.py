from pprint import pprint
import numpy as np

with open('../data/day15.txt') as f:
# with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')

def parse(line):
    sensor_str, beacon_str = line.split(':')
    s_y = eval(sensor_str.split('y=')[1].split(',')[0])
    s_x = eval(sensor_str.split('x=')[1].split(',')[0])
    b_y = eval(beacon_str.split('y=')[1].split(',')[0])
    b_x = eval(beacon_str.split('x=')[1].split(',')[0])
    return (s_x, s_y, b_x, b_y)

def dist(s_x, s_y, b_x, b_y):
    return  abs(s_x - b_x) + abs(s_y - b_y)


"""
dist = 5
dy = 3 = Y - s_y = 4 - 1
intY = 5 = 2 * (dist - dy) + 1 = 2 * (5 - 3) + 1
# # # # # # . .
# # # S # # # #
# # # # # # # B
# # # # # # # .
--#-#-#-#-#----
. . # # # . . .
. . . # . . . .
. . . . . . . .
"""

# Y = 10
Y = 2000000

sensors = [parse(line) for line in lines]
dists = [dist(s[0], s[1], s[2], s[3]) for s in sensors]
intervals = []
for i, s in enumerate(sensors):
    dy = abs(s[1] - Y)
    if dists[i] >= dy:
        intervals.append((s[0] - (dists[i] - dy), s[0] + (dists[i] - dy)))

overlap = set()
for i in intervals:
    overlap.update(range(i[0], i[1] + 1))

# remove positions that are actually a beacon
for s in sensors:
    if s[3] == Y:
        overlap.discard(s[2])

# print(overlap)
print(f'Part 1\n{len(overlap)}')

# Part 2
row_set = set(range(4000000))
for Y in range(4000000):
    intervals = []
    for i, s in enumerate(sensors):
        dy = abs(s[1] - Y)
        if dists[i] >= dy:
            intervals.append((s[0] - (dists[i] - dy), s[0] + (dists[i] - dy)))

    overlap = set()
    for i in intervals:
        overlap.update(range(i[0], i[1] + 1))
    if len(overlap.intersection(row_set)) != len(row_set):
        # take the original set
        original = overlap.copy()
        overlap.update(row_set)
        x = ((original^overlap)&overlap).pop()
        print()
        print(f'Part 2\n{4000000 * x + Y}')
        break
        # trimmed = total.intersection()
    if Y % 100000 == 0:
        print(Y)


    
