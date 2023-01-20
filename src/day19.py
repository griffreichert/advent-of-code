import re
from functools import cache
from collections import deque
with open('../data/day19.txt', 'r') as f:
    lines = f.readlines()
    
blueprints = []
# define robot costs as a tuple (ore, clay, obsidian)
for line in lines:
    nums = [int(i) for i in re.findall('\d+', line)]
    # print(nums)
    blueprints.append((
        # be greedy: prioritize building geode robots first, then obsidian, then clay, then ore
        (nums[5], 0, nums[6], 0), # Geode Robot
        (nums[3], nums[4], 0, 0), # Obsidian Robot
        (nums[2], 0, 0, 0), # Clay Robot
        (nums[1], 0, 0, 0), # Ore Robot
    ))
    
print(blueprints[0])
    
def get_max_costs(blueprint):
    return tuple(max(a, b, c, d) for a, b, c, d in zip(*blueprint))

def collect_geodes(blueprint, robots=(1,0,0,0), resources=(0,0,0,0), toc=24):
    # given the blueprint, find the maximum ammount of robots you could need for each mineral
    # no point building 8 ore robots if the most ore you can spend in a turn is 4
    maxcosts = get_max_costs(blueprint)
    # queue for bfs
    queue = deque()
    queue.add((toc, robots, resources))
    # set to memoize states 
    seen = set()
    best_geodes = 0
    
    while queue:
        state = queue.popleft()
        if state in seen:
            return seen
        toc, robots, resources = state
    # Return the number of geodes collected when you run out of time to make more robots
    if toc == 1:
        return resources[3] + robots[3]
    
    # Collect resources with existing robots
    new_resources = tuple(x + y for x, y in zip(resources, robots))
    # print('\ndont build')
    # print(new_resources)
    # Default to building no new robots in the current minute    
    best_geodes = collect_geodes(blueprint, maxcosts, toc - 1, robots, new_resources)

    # Start building a new robot if possible
    for r, costs in enumerate(blueprint):
        # if you can afford to build a robot, try it and add the number of geodes to the list of possible outcomes
        # (note that you use the resources you had before you started collecting)
        if all(x <= y for x, y in zip(costs, resources)):
            
            # Optimization: dont build more robots if you have more of that robot than the max cost
            mineral_idx = 4 - (r + 1)
            if r > 0 and robots[mineral_idx] >= maxcosts[mineral_idx]:
                continue
            # print('\ninvestigating', r, costs)
            # print('resources:', resources)
            # pay cost of new robot
            new_resources = tuple(x - y for x, y in zip(new_resources, costs))
            # build the new robot, increment the index in the robots tuple corresponding to the new one
            # EX: robots=(1, 0, 2, 0), build a clay robot, new_robots=(1, 1, 2, 0)
            new_robots = tuple(
                x + y for x, y in zip(robots, 
                                      tuple(reversed([1 if i == r else 0 for i in range(4)]))))
            best_geodes = max(best_geodes, collect_geodes(blueprint, maxcosts, toc - 1, new_robots, new_resources))
            
            # BE GREEDY: if you can afford to build a geode robot, always do it, skip building other robots
            if r == 0:
                return best_geodes
            
    return best_geodes
    
test_cases = (
    ((1, 4, 2, 2), (5, 37, 6, 7)),  # minute 24
    ((1, 4, 2, 2), (4, 33, 4, 5)),
    ((1, 4, 2, 2), (3, 29, 2, 3)),
    ((1, 4, 2, 1), (3, 29, 2, 3)),
)
print('test case 1')
g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 1, (1, 4, 2, 2), (5, 37, 6, 7))
assert g == 9, f'!!! failed ({g})'
print('test case 2')
g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 2, (1, 4, 2, 2), (4, 33, 4, 5))
assert g == 9, f'!!! failed ({g})'
print('test case 3')
g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 3, (1, 4, 2, 2), (3, 29, 2, 3))
assert g == 9, g

# print('test case 4')
# print('test case 5')
# print('test case 6')
# print('test case 7')
g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 24)
print(g)

# # Recursive implementation that was too slow
# @cache
# def collect_geodes(blueprint, maxcosts, toc, robots=(1,0,0,0), resources=(0,0,0,0)):
#     """Dynamic programming algorithm to collect the most geodes in the time constraint
    
#     Parameters:
#         - blueprint: tuple representing tuples of costs for each robot 
#                     (ore robot, clay robot, obsidian robot, geode robot)
#         - maxcosts: the most of a resource you could need to build another robot
#         - toc: minutes of time remaining
#         - robots: tuple representing the number of each type of robot you have
#         - resources: tuple representing the number of each type of resource you have collected
#     """
#     print(robots, resources)
#     # print(resources)
#     # Base case: return the number of geodes collected when you run out of time
#     if toc == 1:
#         # print('\ncollected', resources[3] + robots[3], 'geodes')
#         # print(robots)
#         return resources[3] + robots[3]
    
#     # Collect resources with existing robots
#     new_resources = tuple(x + y for x, y in zip(resources, robots))
#     # print('\ndont build')
#     # print(new_resources)
#     # Default to building no new robots in the current minute    
#     best_geodes = collect_geodes(blueprint, maxcosts, toc - 1, robots, new_resources)

#     # Start building a new robot if possible
#     for r, costs in enumerate(blueprint):
#         # if you can afford to build a robot, try it and add the number of geodes to the list of possible outcomes
#         # (note that you use the resources you had before you started collecting)
#         if all(x <= y for x, y in zip(costs, resources)):
            
#             # Optimization: dont build more robots if you have more of that robot than the max cost
#             mineral_idx = 4 - (r + 1)
#             if r > 0 and robots[mineral_idx] >= maxcosts[mineral_idx]:
#                 continue
#             # print('\ninvestigating', r, costs)
#             # print('resources:', resources)
#             # pay cost of new robot
#             new_resources = tuple(x - y for x, y in zip(new_resources, costs))
#             # build the new robot, increment the index in the robots tuple corresponding to the new one
#             # EX: robots=(1, 0, 2, 0), build a clay robot, new_robots=(1, 1, 2, 0)
#             new_robots = tuple(
#                 x + y for x, y in zip(robots, 
#                                       tuple(reversed([1 if i == r else 0 for i in range(4)]))))
#             best_geodes = max(best_geodes, collect_geodes(blueprint, maxcosts, toc - 1, new_robots, new_resources))
            
#             # BE GREEDY: if you can afford to build a geode robot, always do it, skip building other robots
#             if r == 0:
#                 return best_geodes
            
#     return best_geodes
    
# def get_max_costs(blueprint):
#     return tuple(max(a, b, c, d) for a, b, c, d in zip(*blueprint))

# test_cases = (
#     ((1, 4, 2, 2), (5, 37, 6, 7)),  # minute 24
#     ((1, 4, 2, 2), (4, 33, 4, 5)),
#     ((1, 4, 2, 2), (3, 29, 2, 3)),
#     ((1, 4, 2, 1), (3, 29, 2, 3)),
# )
# print('test case 1')
# g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 1, (1, 4, 2, 2), (5, 37, 6, 7))
# assert g == 9, f'!!! failed ({g})'
# print('test case 2')
# g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 2, (1, 4, 2, 2), (4, 33, 4, 5))
# assert g == 9, f'!!! failed ({g})'
# print('test case 3')
# g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 3, (1, 4, 2, 2), (3, 29, 2, 3))
# assert g == 9, g

# # print('test case 4')
# # print('test case 5')
# # print('test case 6')
# # print('test case 7')
# g = collect_geodes(blueprints[0], get_max_costs(blueprints[0]), 24)
# print(g)

# # print()
# # print(get_max_costs(blueprints[0]))