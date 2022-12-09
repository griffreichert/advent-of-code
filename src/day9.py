import numpy as np
import math

with open('../data/example.txt', 'r') as f:
    lines = [line for line in f]

class Rope:
    
    def __init__(self, shape):
        self.shape = shape
        self.grid = np.full(self.shape, '.')
        self.visited = np.zeros(self.shape, dtype=int)
        self.head = (int(self.shape[0]/2),int(self.shape[1]/2))
        self.tail = self.head
        # self.grid = np.full((5, 6), '.')
        # self.update_grid()
        self.mark_tail()
    
    # def update_grid(self):
    #     self.grid = np.full((5, 6), '.')
    #     self.grid[self.tail] = 'T'
    #     self.grid[self.head] = 'H'
        
    def mark_tail(self):
        self.visited[self.tail] = 1
        
    def show(self):
        ANSI_COLOR = '\033[92m'
        ANSI_END = '\033[0m'
        self.grid = np.full(self.shape, '.')
        self.grid[self.tail] = 'T'
        self.grid[self.head] = 'H'
        for i in range(len(self.grid)):
            print(' '.join(self.grid[i]), end='    ')
            print(' '.join([f'{v}' if v == 0 else f'{ANSI_COLOR}{v}{ANSI_END}' for v in self.visited[i]]))
        print()
    def move_rope(self, operation, verbose=0):
        direction, magnitude = operation.replace('\n', '').split(' ')
        
        for i in range(int(magnitude)):
            # copy current head position before moving it (to update tail later if needed)
            old_head = self.head
            # move up
            if direction == 'U':
                self.head = (self.head[0] - 1, self.head[1])
            # move down
            elif direction == 'D':
                self.head = (self.head[0] + 1, self.head[1])
            # move right
            elif direction == 'R':
                self.head = (self.head[0], self.head[1] + 1)
            # move left
            elif direction == 'L':
                self.head = (self.head[0], self.head[1] - 1)
            if verbose==2:
                print('--------------------------')
                self.show()
            
            # if rope is not touching, move the tail to where the head used to be
            if self.plank_dist() > 2:
                self.tail = old_head
                    
            self.mark_tail()
            if verbose==2:
                self.show()
                print()
                
        if verbose==1:
            print('--------------------------')
            print(operation, end='')
            self.show()
            
    def plank_dist(self):
        return int(math.dist(self.head, self.tail)**2)
            
    def count_visited(self):
        return np.sum(self.visited)
    
        
r = Rope(shape=(1000, 1000))
# r.show()
with open('../data/day9.txt', 'r') as f:
# with open('../data/example.txt', 'r') as f:
    for line in f:
        r.move_rope(line, verbose=0)
print(r.count_visited())