import math
import numpy as np

register = []
with open('../data/day10.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        register.append(0)
        if line != 'noop':
            register.append(int(line.split(' ')[1]))

x = [1]
for i in range(len(register)):
    x.append(x[-1] + register[i])

cycles = [20, 60, 100, 140, 180, 220]
total = sum([x[c-1] * c for c in cycles])
print(f'\nPart 1\n{total}')
print('\nPart 2\n')

class Screen:
    def __init__(self) -> None:
        self.screen = np.zeros((6, 40), dtype='int')

    def show(self):
        for row in self.screen:
            print(''.join(['#' if pix == 1 else ' ' for pix in row]))
        print()

    def pos_2d(self, pos):
        return (math.floor(pos/40), pos % 40)

    def draw(self, x):
        for i in range(len(x)):
            sprite_mid = x[i]
            cur = self.pos_2d(i)
            if abs(sprite_mid - cur[1]) <= 1:
                self.screen[cur] = 1
        self.show()

Screen().draw(x)