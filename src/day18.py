from collections import defaultdict

with open('../data/day18.txt') as f:
    lines = f.read().strip().split('\n')

o = defaultdict(int)

cubes = set()
for line in lines:
    tup = tuple(eval(i) for i in line.split(','))
    cubes.add(tup)
    o[tup] = 1

print(cubes)

neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

# surface area
sa = 0
for cx, cy, cz in cubes:
    # print(cx)
    for nx, ny, nz in neighbors:
        x = cx + nx
        y = cy + ny
        z = cz + nz
        if o[x, y, z] == 0:
            sa += 1
    # print(c)
print(sa)
# max_x = 0
# max_y = 0
# max_z = 0
# for c in cube_list:
#     max_x = max(max_x, c[0])
#     max_y = max(max_y, c[1])
#     max_z = max(max_z, c[2])

# print(cube_list)
# # print(max_x, max_y, max_z)

# x = np.zeros((max_y, max_z), dtype=np.int8)
# y = np.zeros((max_x, max_z), dtype=np.int8)
# z = np.zeros((max_x, max_y), dtype=np.int8)

# for c in cube_list:
#     cx = c[0] - 1
#     cy = c[1] - 1
#     cz = c[2] - 1
#     x[cy][cz] = 1
#     y[cx][cz] = 1
#     z[cx][cy] = 1

# print(f'x: {np.sum(x)}  y: {np.sum(y)}  z: {np.sum(z)}')
# print(2*np.sum(x) + 2*np.sum(y) + 2*np.sum(z))