from pprint import pprint

with open('../data/day14.txt') as f:
    lines = f.read().strip().split('\n')
    
rocks = [[eval(coord) for coord in l.split('->')] for l in lines]

class Cave:
    def __init__(self, rocks):
        max_depth = 0
        for r in rocks:
            for tup in r:
                if tup[1] > max_depth:
                    max_depth = tup[1]
                    
        max_left = 500 - 2*max_depth
        max_right = 500 + 2*max_depth
        row_width = max_right - max_left
                    
        self.shift = max_left + 1
        self.cave = [['.']*(row_width) for _ in range(max_depth+2)]
        self.cave.append(['#']*(row_width))
        self.drop_point = 500 - self.shift
        self.cave[0][self.drop_point] = '+'
        self.n = len(self.cave)
        self.m = len(self.cave[0])
        self.grains = 0
        self.create_rocks(rocks)
        
    def create_rocks(self, rocks):
        for rock in rocks:
            for r in range(len(rock) - 1):
                cur_i = rock[r][1] 
                cur_j = rock[r][0] - self.shift
                nxt_i = rock[r+1][1] 
                nxt_j = rock[r+1][0] - self.shift
                for i in range(min(cur_i, nxt_i), max(cur_i, nxt_i) + 1):
                    self.cave[i][cur_j] = '#'
                for j in range(min(cur_j, nxt_j), max(cur_j, nxt_j) + 1):
                    self.cave[cur_i][j] = '#'
    
    def fill_sand(self):
        while True:
            # drop a grain of sand starting at the drop point
            i = 0
            j = self.drop_point
            while True:
                # if sand hits the row of air above the floor, return the number of grains of sand that it took
                if i+1 == self.n - 1:
                    return self.grains
                # if space below is air, move sand down one
                if self.cave[i+1][j] == '.':
                    i += 1
                    continue
                # otherwise the space below is blocked
                # if left is not blocked
                if self.cave[i+1][j-1] == '.':
                    i += 1
                    j -= 1
                    continue
                # if right is air
                if self.cave[i+1][j+1] == '.':
                    i += 1
                    j += 1
                    continue
                # if none of those conditions are true, then you are no longer falling
                break
            self.cave[i][j] = 'o'
            self.grains +=1
    
    def fill_sand_pt2(self):
        while True:
            # drop a grain of sand
            i = 0
            j = self.drop_point
            while True:
                if self.cave[0][self.drop_point] == 'o':
                    return self.grains
                # if space below is air, move sand down one
                if self.cave[i+1][j] == '.':
                    i += 1
                    continue
                # otherwise the space below is blocked
                # if left is not blocked
                if self.cave[i+1][j-1] == '.':
                    i += 1
                    j -= 1
                    continue
                # if right is air
                if self.cave[i+1][j+1] == '.':
                    i += 1
                    j += 1
                    continue
                # if none of those conditions are true, then you are no longer falling
                break
            self.cave[i][j] = 'o'
            self.grains +=1

    def show(self):
        print()
        for row in self.cave:
            print(''.join(row))  
        print()      

c = Cave(rocks)
c.show()
grains = c.fill_sand()
c.show()
print(grains)
grains = c.fill_sand_pt2()
c.show()
print(grains)