import numpy as np
import pandas as pd

with open('../data/day8.txt', 'r') as f:
    lines = [str(line).replace('\n', '') for line in f]

class Forest():
    def __init__(self, lines):
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.forest = np.zeros((self.rows, self.cols)).astype(int)
        self.scenic = np.zeros((self.rows, self.cols)).astype(int)
        # create forest object as ndarray 
        for row in range(self.rows):
            for col in range(self.cols):
                self.forest[row, col] = int(lines[row][col])
    
    @property
    def show(self):
        print(self.forest)            
    
    @property
    def show_scenic(self):
        print(self.scenic)            
        
    def count_visible(self):
        ANSI_COLOR = '\033[92m'
        ANSI_END = '\033[0m'

        visible = 2*self.rows + 2*(self.cols-2)
        for tree in self.forest[0]:
            print(tree, end=' ')
        print()
        for row in range(1, self.rows-1):
            print(self.forest[row,0], end=' ')
            for col in range(1, self.cols-1):
                cur_vis = self.check_visible(row, col)
                if cur_vis:
                    print(ANSI_COLOR + str(self.forest[row,col]) + ANSI_END, end=' ')
                else:
                    print(str(self.forest[row,col]), end=' ')
                visible += cur_vis
            print(self.forest[row,-1])
        for tree in self.forest[-1]:
            print(tree, end=' ')
        print()
        return visible
    
    def check_visible(self, row, col):
        if any([self.check_north(row, col), self.check_south(row, col),
                self.check_east(row, col), self.check_west(row, col)]):
            return 1
        return 0
    
    def check_north(self, row, col):
        return max(self.forest[0:row, col]) < self.forest[row, col]
    
    def check_south(self, row, col):
        return max(self.forest[row+1:self.rows+1, col]) < self.forest[row, col]
        
    def check_east(self, row, col):
        return max(self.forest[row, col+1:self.cols+1]) < self.forest[row, col]

    def check_west(self, row, col):
        return max(self.forest[row, 0:col]) < self.forest[row, col]

    def max_scenic_score(self):
        self.generate_scenic_scores()
        return np.max(self.scenic)
    
    def generate_scenic_scores(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.scenic[row, col] = self.score_north(row, col) * self.score_south(row, col) * self.score_east(row, col) * self.score_west(row, col)
        self.show_scenic
        
    def score_north(self, row, col):
        north = self.forest[0:row, col]
        north = north[::-1]
        for i in range(len(north)):
            if north[i] >= self.forest[row, col]:
                return i + 1
        return len(north)
        
    def score_south(self, row, col):
        south = self.forest[row+1:self.rows+1, col]
        for i in range(len(south)):
            if south[i] >= self.forest[row, col]:
                return i + 1
        return len(south)

    def score_east(self, row, col):
        east = self.forest[row, col+1:self.cols+1]
        for i in range(len(east)):
            if east[i] >= self.forest[row, col]:
                return i + 1
        return len(east)

        
    def score_west(self, row, col):
        west = self.forest[row, 0:col]
        west = west[::-1]
        for i in range(len(west)):
            if west[i] >= self.forest[row, col]:
                return i + 1
        return len(west)
        
    
forest = Forest(lines)
visible = forest.count_visible()
print(f'\nPart 1\n{visible} visible trees\n')

scenic = forest.max_scenic_score()
print(f'\nPart 2\n{scenic} best scenic score\n')
