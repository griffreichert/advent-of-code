import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint

with open(f"../data/day19.txt", "r") as f:
    scanners = [
        [
            tuple(int(i) for i in s.split(","))
            for s in scanner.split("\n")
            if "---" not in s
        ]
        for scanner in f.read().strip().split("\n\n")
    ]
print(scanners)


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
