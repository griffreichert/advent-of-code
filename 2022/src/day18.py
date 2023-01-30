from collections import defaultdict

with open('../data/day18.txt') as f:
# with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')

d = defaultdict(int)

cubes = set()
for line in lines:
    tup = tuple(eval(i) for i in line.split(','))
    cubes.add(tup)
    d[tup] = 1

# print(cubes)

neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

# surface area
sa = 0
for cx, cy, cz in cubes:
    for nx, ny, nz in neighbors:
        x = cx + nx
        y = cy + ny
        z = cz + nz
        if d[x, y, z] == 0:
            sa += 1

print('Part 1:', sa)

OUTSIDE_AIR = 2

def dfs(x, y, z):
    stack = [(x, y, z)]
    while len(stack) > 0:
        x, y, z = stack.pop()
        if x not in range(-2, 21):
            continue
        if y not in range(-2, 21):
            continue
        if z not in range(-2, 21):
            continue
        if d[x, y, z]:
            continue
        d[x, y, z] = OUTSIDE_AIR
        for nx, ny, nz in neighbors:
            stack.append((
                x + nx,
                y + ny,
                z + nz
            ))

dfs(-2, -2, -2)

# surface area
sa = 0
for cx, cy, cz in cubes:
    for nx, ny, nz in neighbors:
        x = cx + nx
        y = cy + ny
        z = cz + nz
        if d[x, y, z] == OUTSIDE_AIR:
            sa += 1

print('Part 2:', sa)

# cube positions range from 0 to 19
# example cube positions range from 1 to 6

# minx, miny, minz, maxx, maxy, maxz = 1, 1, 1, 1, 1, 1
# for cx, cy, cz in cubes:
#     minx = min(minx, cx)
#     maxx = max(maxx, cx)
#     miny = min(miny, cy)
#     maxy = max(maxy, cy)
#     minz = min(minz, cz)
#     maxz = max(maxz, cz)

# print(minx, maxx)
# print(miny, maxy)
# print(minz, maxz)