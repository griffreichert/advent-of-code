import string
from collections import defaultdict
from aoc_tools import *
import functools
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"../data/example.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

g = {}
f = {}
for line in s.split("\n"):
    valve = line[6:8]
    flow = nums(line)[0]
    _, r = line.split(";")
    r = r.replace("valves","valve")[len(" tunnels lead to valve "):]
    g[valve] = r.split(", ")
    f[valve] = flow

cur = "AA"

@functools.lru_cache(maxsize=None)
def maxflow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    best = 0
    if cur not in opened:
        val = (min_left - 1) * f[cur]
        cur_opened = tuple(sorted(opened + (cur,)))
        for adj in g[cur]:
            if val != 0:
                best = max(best,
                    val + maxflow(adj, cur_opened, min_left - 2))
            best = max(best,
                maxflow(adj, opened, min_left - 1))
    return best

print(maxflow("AA", (), 30))