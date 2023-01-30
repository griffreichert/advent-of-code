# import functools
from functools import cache
from pprint import pprint
import re

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
def max_pressure(cur, opened, toc, elephant_time=False):
    """Recursive algorithm to find the maximum possible pressure to release in advent of code day 16

    Parameters:
        - cur: string representing the tuple you are currently at
        - opened: a tuple containing all of the valves that have been opened. ex: ('AA', 'BB'), important for caching that it is hashable
        - toc: int representing the number of minutes remaining
    """
    # base case: when time runs out
    if toc == 0:
        # solution to pt 2
        if elephant_time:
            """
            For part 2, we as the human take the optimal path to release as much pressure as possible
            When we run out of time, we then send the elephant to essentially go over the path and get any valves we missed 
            """
            return max_pressure('AA', opened, 26, False)
        return 0
    
    # Option 1: dont open the valve and go to neighbors
    best_if_walk = max([max_pressure(adj, opened, toc - 1, elephant_time) for adj in tunnels[cur]])
    best_if_open = 0
    
    # Option 2: only open valves that will release pressure and that we have not opened previously
    if cur not in opened and flow[cur] > 0:
        # add current valve to set of open valves
        new_opened = tuple(opened) + (cur,)
        # if you open the valve you get the pressure of the valve... 
        best_if_open = flow[cur] * (toc - 1)
        # ...plus your best option with time remaining
        best_if_open += max_pressure(cur, frozenset(new_opened), toc - 1, elephant_time)
    return max(best_if_open, best_if_walk)

print('Part 1:', max_pressure('AA', frozenset(), 30))
print('Part 2:', max_pressure('AA', frozenset(), 26, True))