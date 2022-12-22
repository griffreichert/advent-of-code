import functools
from pprint import pprint

# with open('../data/day16.txt') as f:
with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')

# dict to hold which valves tunnel to which valves
tunnels = {}
# dict to hold each valve and it's flow rate
flow = {}
for l in lines:
    v = l[6:8]
    flow[v] = eval(l.split('=')[1].split(';')[0])
    tunnels[v] = l.replace('valve ', 'valves ').split('valves ')[1].split(', ')

# @functools.lru_cache(maxsize=None)
# def max_pressure(cur, opened, min):
#     # base case: when time runs out
#     if min <= 0:
#         return 0
#     best = 0
#     if cur not in opened:
#         cur_pressure = (min - 1) * flow[cur]
#         cur_opened = opened + (cur,)
#         # print(cur_opened)
#         for adj in tunnels[cur]:
#             # if you open cur (only open it if flow > 0)
#             if flow[cur] != 0:
#                 best = max(best, cur_pressure + max_pressure(adj, cur_opened, min - 2))
#             # if you dont open cur
#             best = max(best, max_pressure(adj, opened, min - 1))
#     return best
        
# print(max_pressure('AA', (), 30))

# pprint(flow)
# pprint(tunnels)

@functools.lru_cache(maxsize=None)
def maxflow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    best = 0
    if cur not in opened:
        val = (min_left - 1) * flow[cur]
        cur_opened = tuple(sorted(opened + (cur,)))
        for adj in tunnels[cur]:
            if val != 0:
                best = max(best,
                    val + maxflow(adj, cur_opened, min_left - 2))
            best = max(best,
                maxflow(adj, opened, min_left - 1))
    return best

print(maxflow("AA", (), 30))
