import re
from functools import cache
from collections import deque
import time

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

test_blueprint = (
    (2, 0, 7, 0),
    (3, 14, 0, 0),
    (2, 0, 0, 0),
    (4, 0, 0, 0),
)    

# print(blueprints[0])
    
def get_max_costs(blueprint):
    return tuple(max(a, b, c, d) for a, b, c, d in zip(*blueprint))

def collect_geodes(blueprint, robots=(1,0,0,0), resources=(0,0,0,0), toc=24):
    # given the blueprint, find the maximum ammount of robots you could need for each mineral
    # no point building 8 ore robots if the most ore you can spend in a turn is 4
    maxcosts = get_max_costs(blueprint)
    # queue for bfs
    queue = deque()
    queue.append((toc, robots, resources))
    # set to memoize states 
    seen = set()
    best_geodes = 0
    
    while queue:
        state = queue.popleft()

        # prune queue if we have seen this state before
        if state in seen:
            continue
        seen.add(state)

        # if len(queue) % 10000 == 0:
        #     print(state, len(queue))

        toc, robots, resources = state
        
        # if we run out of time stop searching
        if toc == 1:
            # update best geodes accordingly: number you have plus what you can make in the final minute
            best_geodes = max(best_geodes, resources[3] + robots[3])
            continue
        
        # Collect resources with existing robots
        collected_resources = tuple(x + y for x, y in zip(resources, robots))
        # Cap collected resources if the ammount you have is more than you could ever spend (this prunes queue)
        maxspend = tuple(toc * cost if cost != 0 else 99 for cost in maxcosts)
        collected_resources = tuple(min(x, y) for x, y in zip(maxspend, collected_resources))
       
        # Default to building no new robots in the current minute    
        queue.append((toc - 1, robots, collected_resources))

        # Start building a new robot if possible
        for r, costs in enumerate(blueprint):
            # if you can afford to build a robot, try it and add the number of geodes to the list of possible outcomes
            # (note that you use the resources you had before you started collecting)
            if all(x <= y for x, y in zip(costs, resources)):
                
                # Optimization: dont build more robots if you have more of that robot than the max cost
                mineral_idx = 4 - (r + 1)
                if r > 0 and robots[mineral_idx] >= maxcosts[mineral_idx]:
                    continue

                # pay cost of new robot
                resources_post_cost = tuple(x - y for x, y in zip(collected_resources, costs))
                # build the new robot, increment the index in the robots tuple corresponding to the new one
                # EX: robots=(1, 0, 2, 0), build a clay robot, new_robots=(1, 1, 2, 0)
                assert all(res >= 0 for res in resources_post_cost), (state, costs, resources_post_cost)
                new_robots = tuple(
                    x + y for x, y in zip(robots, 
                                        tuple(reversed([1 if i == r else 0 for i in range(4)]))))
                queue.append((toc - 1, new_robots, resources_post_cost))
                
                # # BE GREEDY: if you can afford to build a geode robot, always do it, skip building other robots
                if r == 0:
                    break
    return best_geodes

total = 0
for b, blueprint in enumerate(blueprints):
    # print(b+1)
    total += (b + 1) * (collect_geodes(blueprint))

print('Part 1:', total)

total = 1
for b, blueprint in enumerate(blueprints[:3]):
    # print(b+1)
    g = collect_geodes(blueprint, toc=32)
    total *= g

print('Part 2:', total)

# # Recursive implementation that was  slower than stack based
# @cache
# def collect_geodes_rec(blueprint, maxcosts, toc=24, robots=(1,0,0,0), resources=(0,0,0,0)):
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
#     # Base case: return the number of geodes collected when you run out of time
#     if toc == 1:
#         return resources[3] + robots[3]
    
#     # Collect resources with existing robots
#     new_resources = tuple(x + y for x, y in zip(resources, robots))
#     # Default to building no new robots in the current minute    
#     best_geodes = collect_geodes_rec(blueprint, maxcosts, toc - 1, robots, new_resources)

#     # Start building a new robot if possible
#     for r, costs in enumerate(blueprint):
#         # if you can afford to build a robot, try it and add the number of geodes to the list of possible outcomes
#         # (note that you use the resources you had before you started collecting)
#         if all(x <= y for x, y in zip(costs, resources)):
#             # Optimization: dont build more robots if you have more of that robot than the max cost
#             mineral_idx = 4 - (r + 1)
#             if r > 0 and robots[mineral_idx] >= maxcosts[mineral_idx]:
#                 continue
#             # pay cost of new robot
#             resources_post_cost = tuple(x - y for x, y in zip(new_resources, costs))
#             # build the new robot, increment the index in the robots tuple corresponding to the new one
#             # EX: robots=(1, 0, 2, 0), build a clay robot, new_robots=(1, 1, 2, 0)
#             new_robots = tuple(
#                 x + y for x, y in zip(robots, 
#                                       tuple(reversed([1 if i == r else 0 for i in range(4)]))))
#             best_geodes = max(best_geodes, collect_geodes_rec(blueprint, maxcosts, toc - 1, new_robots, resources_post_cost))
            
#             # Greedy Heuristic: if you can afford to build a geode robot, always do it, skip building other robots
#             if r == 0:
#                 break
#     return best_geodes

# rec_start = time.time()
# print(collect_geodes_rec(test_blueprint, get_max_costs(test_blueprint)))
# rec_end = time.time()
# rec_time = rec_end - rec_start
# print('Rec time:', rec_time, 'seconds')

# stack_start = time.time()
# print(collect_geodes(test_blueprint))
# stack_end = time.time()
# stack_time = stack_end - stack_start
# print('Stack time:', stack_time, 'seconds')