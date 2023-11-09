import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint


lines = utils.read_list(__file__, as_str=True)
(x1, x2), (y1, y2) = tuple(
    tuple(int(i) for i in chunk[2:].split("..")) for chunk in lines[0][13:].split(", ")
)

# y1, y2 = min(y_coords), max(y_coords)
# x1, x2 = min(x_coords), max(x_coords)

print(x1, x2)
print(y1, y2)


def p1():
    res = 0
    return res


def p2():
    res = 0
    return res


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
