import numpy as np
from string import ascii_lowercase
from heapq import heappop,  heappush

map = []
# with open('../data/example.txt') as f:
with open('../data/day12.txt') as f:
    for line in f:
        map.append([c for c in line[0:-1]])


# create numpy array of the map
class Grid:
    def __init__(self, map) -> None:
        self.shape = (len(map), len(map[0]))
        self.grid = np.zeros(self.shape, dtype='int')
        self.start = (0,0)
        self.end = (0,0)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                # mark start and end points
                if map[i][j] == 'S':
                    self.start = (i, j)
                    self.grid[i,j] = 0
                elif map[i][j] == 'E':
                    self.end = (i, j)
                    self.grid[i,j] = 25
                else:
                    self.grid[i,j] = ascii_lowercase.index(map[i][j])

        print(self.start, self.end)

    def shortest_path(self):
        # dijkstras shortest path algorithm
        visited = np.zeros(self.shape, dtype='int')
        # initialise heap
        heap = [(0, self.start, [self.start])]

        while True:
            cost, pos, path = heappop(heap)
            
            # if you have already visited this cell, skip as there is a shorter path to get to it already in the heap
            if visited[pos] == 1:
                continue
            
            # mark current cell as visited
            visited[pos] = 1
            
            # base case, return when you have found the end
            if pos == self.end:
                # print the path
                print()
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        p = '.'
                        if (i, j) in path:
                            p = '*'
                        if (i, j) == self.start:
                            p = 'S'
                        if (i, j) == self.end:
                            p ='$'
                        print(p, end=' ')
                    print()
                return cost, path

            # add adjacent cells to the stack if not greater than cur + 1, within bounds
            for tup in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = pos[0] + tup[0]
                jj = pos[1] + tup[1]
                if 0 <= ii < self.shape[0] and 0 <= jj < self.shape[1]:
                    if (self.grid[pos] + 1 >= self.grid[ii, jj]):
                        heappush(heap, (cost + 1, (ii, jj), path + [(ii, jj)]))

    def shortest_path_pt2(self):
        # dijkstras shortest path algorithm
        visited = np.zeros(self.shape, dtype='int')
        # initialise heap
        heap = [(0, self.end, [self.end])]

        while True:
            cost, pos, path = heappop(heap)
            
            # if you have already visited this cell, skip as there is a shorter path to get to it already in the heap
            if visited[pos] == 1:
                continue
            
            # mark current cell as visited
            visited[pos] = 1
            
            # base case, return when you have found a cell at elevation 0
            if self.grid[pos] == 0:
                # print the path
                print()
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        p = '.'
                        if (i, j) in path:
                            p = '*'
                        if (i, j) == self.end:
                            p = 'S'
                        if (i, j) == pos:
                            p = 'a'
                        print(p, end=' ')
                    print()
                return cost, path

            # add adjacent cells to the stack if not less than cur - 1, within bounds
            for tup in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = pos[0] + tup[0]
                jj = pos[1] + tup[1]
                if 0 <= ii < self.shape[0] and 0 <= jj < self.shape[1]:
                    if (self.grid[pos] - 1 <= self.grid[ii, jj]):
                        heappush(heap, (cost + 1, (ii, jj), path + [(ii, jj)]))

g = Grid(map)

path_len, path = g.shortest_path()

path_len_2, path_2 = g.shortest_path_pt2()

print(f'\nPart 1\n{path_len}')
print(f'\nPart 2\n{path_len_2}')