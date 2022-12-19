from pprint import pprint

with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')
    
rocks = [[eval(coord) for coord in l.split('->')] for l in lines]

class Cave:
    def __init__(self, rocks):
        max_depth = 0
        max_left = 500
        max_right = 500
        for r in rocks:
            for tup in r:
                if tup[0] < max_left:
                    max_left = tup[0]
                if tup[0] > max_right:
                    max_right = tup[0]
                if tup[1] > max_depth:
                    max_depth = tup[1]
                    
        self.shift = max_left - 1
        self.cave = [['.']*(max_right - max_left + 3) for _ in range(max_depth+2)]
        self.cave[0][500 - self.shift] = '+'
        self.n = len(self.cave)
        self.m = len(self.cave[0])
        self.create_rocks(rocks)
        
    def create_rocks(self, rocks):
        for rock in rocks:
            for r in range(len(rock) - 1):
                cur_i = rock[r][1] 
                cur_j = rock[r][0] - self.shift
                nxt_i = rock[r+1][1] 
                nxt_j = rock[r+1][0] - self.shift
                print(cur_i, nxt_i, cur_j, nxt_j)
                for i in range(min(cur_i, nxt_i), max(cur_i, nxt_i) + 1):
                    self.cave[i][cur_j] = '#'
                for j in range(min(cur_j, nxt_j), max(cur_j, nxt_j) + 1):
                    self.cave[cur_i][j] = '#'
                
    def show(self):
        print()
        for row in self.cave:
            print(' '.join(row))        


c = Cave(rocks)
c.show()
