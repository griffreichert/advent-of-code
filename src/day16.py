# import functools
from functools import cache
from pprint import pprint
import re
c
with open('../data/day16.txt') as f:
    lines = f.read().strip().split('\n')

# lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II""".split('\n')

# dict to hold which valves tunnel to which valves
tunnels = {}
# dict to hold each valve and it's flow rate
flow = {}
for l in lines:
    v = l[6:8]
    flow[v] = int(re.findall("\d+", l)[0])
    tunnels[v] = l.replace('valve ', 'valves ').split('valves ')[1].split(', ')
# pprint(flow)
 
@cache
def max_pressure(cur, opened, toc):
    # base case: when time runs out
    if toc <= 0:
        return 0

    # Option 1: dont open the valve and go to neighbors
    best_if_walk = max([max_pressure(adj, opened, toc - 1) for adj in tunnels[cur]])

    if flow[cur] > 0 and cur not in opened:
        # if you open the valve you get the pressure of the valve, plus your best option with time remaining
        best_if_open = flow[cur] * (toc - 1) + max_pressure(cur, opened + (cur,), toc - 1)
        return max(best_if_open, best_if_walk)
    return best_if_walk

print('Part 1:', max_pressure('AA', (), 30))

@cache
def elephant_in_the_tunnels(h_cur, e_cur, opened, toc):
    # base case: when time runs out
    if toc <= 0:
        return 0

    # 1: do the human
    # Option 1: dont open the valve and go to neighbors
    best_if_walk = max([max_pressure(adj, opened, toc - 1) for adj in tunnels[cur]])

    if flow[cur] > 0 and cur not in opened:
        # if you open the valve you get the pressure of the valve, plus your best option with time remaining
        best_if_open = flow[cur] * (toc - 1) + max_pressure(cur, opened + (cur,), toc - 1)
        return max(best_if_open, best_if_walk)
    return best_if_walk
    # dont move to the same tunnel as the elephant

print('Part 1:', max_pressure('AA', 'AA', (), 26))