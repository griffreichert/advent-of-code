import copy
import pandas as pd
import numpy as np
from pprint import pprint

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
                if ord(map[i][j]) == 83:
                    self.start = (i, j)
                    self.grid[i,j] = 0
                elif ord(map[i][j]) == 69:
                    self.end = (i, j)
                    self.grid[i,j] = 27
                else:
                    self.grid[i,j] = ord(map[i][j]) - 96

        print(self.start, self.end)

    @property    
    def show(self):
        for row in self.grid:
            print(' '.join([f'{i:2d}' for i in row]))

    def shortest_path(self):
        # dijkstras shortest path algorithm
        visited = np.zeros(self.shape, dtype='int')
        queue = [{'cost': self.grid[self.start], 'path':[self.start]}]
        return self.shortest_path_helper(queue, visited)

    def shortest_path_helper(self, queue, visited):
        


        # explore
        cur = queue.pop(0)
        pos = cur['path'][-1]



        # base case, return when you have found the end
        if pos == self.end:
            
            # print the current state
            print(f'\n{pos}')
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    p = '.'
                    if (i, j) in cur['path']:
                        p = '*'
                    if pos == (i, j):
                        p = '@'
                    if self.grid[i][j] == 0:
                        p = 'S'
                    if self.grid[i][j] == 27:
                        p = 'E'
                    if (i, j) == self.end:
                        p ='$'
                    print(p, end=' ')
                print()
            return cur

        # # mark current cell as visited
        # visited[pos] = 1

        # add to adjacent cells to the stack if not greater than cur + 1, within bounds, and has not been visited

        # check north
        north = (pos[0] - 1, pos[1])
        if (north not in cur['path']) and (north[0] >= 0) and (self.grid[north] <= self.grid[pos] + 1) and (self.grid[north] >= self.grid[pos]):
            tmp = cur['path'] + [north]
            queue.append({
                'cost': cur['cost'] + self.grid[north], 
                'path': tmp
            })
        
        # check south
        south = (pos[0] + 1, pos[1])
        # if pos == (4,2):
        #     print('hit it')
        #     print(cur)
        #     print(south)
        #     print(self.grid.shape)
        if (south not in cur['path']) and (south[0] < self.shape[0]) and (self.grid[south] <= self.grid[pos] + 1) and (self.grid[south] >= self.grid[pos]):
            tmp = cur['path'] + [south]
            queue.append({
                'cost': cur['cost'] + self.grid[south], 
                'path': tmp
            })

        # check east
        east = (pos[0], pos[1] + 1)
        if (east not in cur['path']) and (east[1] < self.shape[1]) and (self.grid[east] <= self.grid[pos] + 1) and (self.grid[east] >= self.grid[pos]):
            tmp = cur['path'] + [east]
            queue.append({
                'cost': cur['cost'] + self.grid[east], 
                'path': tmp
            })

        # check west
        west = (pos[0], pos[1] - 1)
        if (west not in cur['path']) and (west[1] >= 0) and (self.grid[west] <= self.grid[pos] + 1) and (self.grid[west] >= self.grid[pos]):
            tmp = cur['path'] + [west]
            queue.append({
                'cost': cur['cost'] + self.grid[west], 
                'path': tmp
            })
        
        # {k: v for k, v in sorted(elves.items(), key=lambda item: -item[1])}
        queue = sorted(queue, key=lambda x: x['cost'])
        # print(f'{queue}')
        return self.shortest_path_helper(queue, visited)

        
        # sort the stack in ascending order
        # move to the cell on the top of the stack
        # add that cells adjacent cells to the stack, sort the stack


g = Grid(map)
g.show

res = g.shortest_path()

print(res)
print(len(res['path']) - 1)