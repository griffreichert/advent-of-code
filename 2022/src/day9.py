import numpy as np

with open('../data/example.txt', 'r') as f:
    lines = [line for line in f]

class Rope:
    
    def __init__(self, shape=(12,12), len=2):
        self.shape = shape
        self.num_knots = len
        self.grid = np.full(self.shape, '.')
        self.visited = np.zeros(self.shape, dtype=int)
        self.start = (int(self.shape[0]/2),int(self.shape[1]/2))
        self.knots = [self.start for i in range(self.num_knots)]
        self.mark_tail()

    def mark_tail(self):
        self.visited[self.knots[-1]] = 1
        
    def show(self):
        ANSI_COLOR = '\033[92m'
        ANSI_END = '\033[0m'
        self.grid = np.full(self.shape, '.')
        self.grid[self.start] = 's'
        for i in reversed(range(1, self.num_knots)):
            self.grid[self.knots[i]] = i
        self.grid[self.knots[0]] = 'H'
        for i in range(self.shape[0]):
            print(' '.join(self.grid[i]), end='    ')
            print(' '.join([f'{v}' if v == 0 else f'{ANSI_COLOR}{v}{ANSI_END}' for v in self.visited[i]]))
        print()

    def move_rope(self, operation, verbose=0):
        direction, magnitude = operation.replace('\n', '').split(' ')
        
        # rope moves in iterations (4 individual steps, not 4 steps at once)
        for i in range(int(magnitude)):

            # # copy current knot positions before moving rope (to update trailing positions later if needed)
            # knots_copy = deepcopy(self.knots)
            # prev_knot = self.knots[0]

            # move first knot
            # move up
            if direction == 'U':
                self.knots[0] = (self.knots[0][0] - 1, self.knots[0][1])
            # move down
            elif direction == 'D':
                self.knots[0] = (self.knots[0][0] + 1, self.knots[0][1])
            # move right
            elif direction == 'R':
                self.knots[0] = (self.knots[0][0], self.knots[0][1] + 1)
            # move left
            elif direction == 'L':
                self.knots[0] = (self.knots[0][0], self.knots[0][1] - 1)
            if verbose == 3:
                print('--------------------------')
                print(operation, end='')
                self.show()
            for k in range(1, self.num_knots):
                d = self.dist_to_prev(k)
                prev_knot = self.knots[k-1]
                cur_knot = self.knots[k]
                if d == 5:
                    new_row = cur_knot[0] + (1 if prev_knot[0] > cur_knot[0] else -1)
                    new_col = cur_knot[1] + (1 if prev_knot[1] > cur_knot[1] else -1)
                    self.knots[k] = (new_row, new_col)

                elif self.dist_to_prev(k) > 2:
                    new_row = cur_knot[0] + int((prev_knot[0] - cur_knot[0])/2)
                    new_col = cur_knot[1] + int((prev_knot[1] - cur_knot[1])/2)
                    self.knots[k] = (new_row, new_col)
                    # prev_knot = self.knots[k]
                if verbose == 3:
                    print(d)
                    # prev_knot = self.knots[k-1]
            
            self.mark_tail()

            if verbose==2:
                print('--------------------------')
                print(operation, end='')
                self.show()
                
        if verbose==1:
            print('--------------------------')
            print(operation, end='')
            self.show()
            
    def dist_to_prev(self, i):
        return int(np.linalg.norm(np.asarray(self.knots[i-1])-np.asarray(self.knots[i]))**2)
        # return int(math.dist(self.knots[i-1], self.knots[i])**2)
            
    def count_visited(self):
        return np.sum(self.visited)
    
        
r = Rope(shape=(500, 500), len=2)
with open('../data/day9.txt', 'r') as f:
    for line in f:
        r.move_rope(line, verbose=0)
print(f'\nPart 1\n{r.count_visited()}')
r2 = Rope(shape=(500, 500), len=10)
with open('../data/day9.txt', 'r') as f:
    for line in f:
        r2.move_rope(line, verbose=0)
print(f'\nPart 2\n{r2.count_visited()}\n')
