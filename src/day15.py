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

print(f'Part 1\n{len(overlap)}')

# Part 2

"""
. . . . . 1 . . . . 2 . . 3 . . 
. . . . . . 1 . . 2 . 2 3 . 3 . 
. . . . . . . 1 2 . . 3 2 . . 3 
. . . . . . . 2 1 . 3 . . 2 . . 
. . . . 4 . . 1 2 3 . . 2 . . . 
1 . . 4 . 4 1 $ 3 2 . 2 . . . . 
. 1 4 . . 1 4 3 . . 2 . . . . . 
. 4 1 . 1 . 3 4 . . . . . . . . 
4 . . 1 . . . 3 4 . . . . . . . 
. 4 . . . . . 4 3 . . . . . . . 
. . 4 . . . 4 . . 3 . . . . . . 

using linear algebra, each diamond has 4 lines (two with posive slope, two with negative)
the point will lie on the only square where two positive lines and two negative lines are both 2 apart

point slope
Y - y1 = m(X - x1)
negative line
Y - (sy +- d) = -1(X - sx)
Y = -X + sx + sy +- d
m = -1  b = (sx + sy +-d)
positive line
Y - (sy +- d) = 1(X - sx)
Y = X + sy - sx +-d
m = 1  b = (sy - sx +-d)
"""

pos_intercepts = []
neg_intercepts = []
for i, s in enumerate(sensors):
    pos_intercepts.extend([s[0] - s[1] + dists[i], s[0] - s[1] - dists[i]])
    neg_intercepts.extend([s[0] + s[1] + dists[i], s[0] + s[1] - dists[i]])

pos = None
neg = None

n = len(pos_intercepts)
for i in range(n):
    for j in range(i + 1, n):
        p_i = pos_intercepts[i]
        p_j = pos_intercepts[j]
        if abs(p_i - p_j) == 2:
            pos = min(p_i, p_j) + 1
        n_i = neg_intercepts[i]
        n_j = neg_intercepts[j]
        if abs(n_i - n_j) == 2:
            neg = min(n_i, n_j) + 1

# find intersection point                # 
x, y = (pos + neg) // 2, (neg - pos) // 2
# print(x, y)
# scale result
res = x * 4000000 + y
print(res)
            
            
##  set based solution that worked on example but was too slow on full input

# row_set = set(range(4000000))
# for Y in range(4000000):
#     intervals = []
#     for i, s in enumerate(sensors):
#         dy = abs(s[1] - Y)
#         if dists[i] >= dy:
#             intervals.append((s[0] - (dists[i] - dy), s[0] + (dists[i] - dy)))

#     overlap = set()
#     for i in intervals:
#         overlap.update(range(i[0], i[1] + 1))
#     if len(overlap.intersection(row_set)) != len(row_set):
#         # take the original set
#         original = overlap.copy()
#         overlap.update(row_set)
#         x = ((original^overlap)&overlap).pop()
#         print()
#         print(f'Part 2\n{4000000 * x + Y}')
#         break
