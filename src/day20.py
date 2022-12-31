import numpy as np
from aoc_tools import *
import copy


with open('../data/day20.txt') as f:
    lines = f.read().strip().split('\n')

enc = [
    1,
    2,
    -3,
    3,
    -2,
    0,
    4,
    2,
]

mix = copy.deepcopy(enc)

n = len(enc)

print(enc)

for i, e in enumerate(enc):
    idx = mix.index(e)
    mv = idx + e
    # if mv < 0:
    #     mv -=1
    tmp = mix.pop(idx)
    if mv % len(mix) == 0:
        mix.append(tmp)
    else:
        mix.insert(mv % len(mix), tmp)
    print(mix, e, idx, mv, mv % n)


# enc = [eval(line) for line in lines]
# print(enc)
print(f'{len(enc) - len(set(enc))} duplicates')
