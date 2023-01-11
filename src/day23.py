import numpy as np
from collections import defaultdict, Counter
import copy

with open('../data/day23.txt') as f:
    lines = f.read().strip().split('\n')


# # Test case: pt1 expects 110, pt2 expects 20
# lines = """..............
# ..............
# .......#......
# .....###.#....
# ...#...#.#....
# ....#...##....
# ...#.###......
# ...##.#.##....
# ....#..#......
# ..............
# ..............
# ..............""".split('\n')

class Grove:
    def __init__(self, lines) -> None:
        self.g = defaultdict(int) # default dict to store the grove
        self.n = len(lines)
        self.m = len(lines[0])
        self.pt1_rounds = 10
        
        for i in range(self.n):
            for j in range(self.m):
                if lines[i][j] == '#':
                    # store elves in default dict with a tuple representing their location
                    self.g[(i, j)] = 1

    def show(self):
        """Prints out the current grove
        """
        x_coords = list(map(lambda x: x[1], self.g.keys()))
        y_coords = list(map(lambda x: x[0], self.g.keys()))
        
        for i in range(min(y_coords), max(y_coords) + 1):
            for j in range(min(x_coords), max(x_coords) + 1):
                print('#' if (i,j) in self.g else '.', end=' ')
            print()
        print()
        
    def unstable_diffusion(self):
        """Move the elves around the grove based on the rules.
        
        Rules:
            During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

            - If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
            - If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
            - If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
            - If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

            After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.
        
        Method:
            while an elf wants to move
            Store current positions
            Record positions of where each elf wants to go to a dict of {(cur elf loc): (desired loc)}
            Create proposed grove with the count of elves that want to go to each position
            for each elf, if their proposed position is less than 1, move them there, otherwise they stay with the same location

        """
        
        N = (-1, 0)
        S = (1, 0)
        E = (0, 1) 
        W = (0, -1)

        NE = (-1, 1)
        NW = (-1, -1)
        SE = (1, 1)
        SW = (1, -1)
        
        dirs = [
            [N, NE, NW],
            [S, SE, SW],
            [W, NW, SW],
            [E, NE, SE],
        ]
        
        for itr in range(10000):
        # for itr in range(self.pt1_rounds):
            
            # create a queue of elves that want to move (have an elf in one of their surrounding spaces)
            queue = []
            for elf in self.g:
                # if there is another elf in one of the surrounding 8 spaces, add the elf to the queue
                if any([tuple(x + y for x, y in zip(elf, n)) in self.g for n in [N, S, E, W, NE, NW, SE, SW]]):
                    queue.append(elf)
            
            if itr % 10 == 0:
                print(itr, '-', len(queue))
            
            # if all elves are happy in their current position, 
            if len(queue) == 0:
                self.show()
                print('satisfied in', itr + 1, 'rounds')
                return 
            
            # Record positions of where each elf wants to go to a dict of {(cur elf loc): (desired loc)
            # default destination for each elf is thier current location
            pos_map = {elf: elf for elf in self.g}

            # move the elves who want to move
            for elf in queue:
                for d in dirs:
                    # try to move in each direction
                    if all([tuple(x + y for x, y in zip(elf, n)) not in self.g for n in d]):
                        pos_map[elf] = tuple(x + y for x, y in zip(elf, d[0]))
                        break
            # Create proposed grove with the count of elves that want to go to each position
            # for each elf, if their proposed position is less than 1, move them there, otherwise they stay with the same location
            proposed = Counter(pos_map.values())
            final = defaultdict(int)
            for elf, dest in pos_map.items():
                if proposed[dest] < 2:
                    final[dest] = 1
                else:
                    final[elf] = 1
            self.g = final 
            
            # at the end of the round, the first direction the Elves considered is moved to the end of the list of directions 
            dirs.append(dirs.pop(0))
            if itr == 9:
                self.eval_pt1()
        self.show()
        
    def eval_pt1(self):
        x_coords = list(map(lambda x: x[1], self.g.keys()))
        y_coords = list(map(lambda x: x[0], self.g.keys()))
        horz = (max(x_coords) - min(x_coords) + 1)
        vert = (max(y_coords) - min(y_coords) + 1)
        area = horz * vert 
        elves = len(self.g)
        print('Part 1:', area - elves)
                
grove = Grove(lines)
grove.show()
grove.unstable_diffusion()
