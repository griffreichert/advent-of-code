import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint


lines = utils.read_list(__file__, as_str=True)
lines1 = [[int(ch) for ch in line if ch.isdigit()] for line in lines]
# print(lines[:5])
_p1 = sum(int(str(f"{line[0]}{line[-1]}")) for line in lines1)

nums_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

lines2 = []
for line in lines:
    line_nums = []
    for i in range(len(line)):
        if str(line[i]).isdigit():
            line_nums.append(int(line[i]))
        for slen in [3, 4, 5]:
            if i + slen - 1 < len(line):
                if line[i : i + slen] in nums_dict:
                    line_nums.append(nums_dict[line[i : i + slen]])
    lines2.append(line_nums)


# for line in lines:
#     line = str(line)
#     for num_str, n in nums_dict.items():
#         if num_str in line:
#             line = line.replace(num_str, f"{n}{num_str[1:]}")
#     lines2.append(line)
lines2 = [f"{line[0]}{line[-1]}" for line in lines2]
# print(lines2)
_p2 = sum(int(line) for line in lines2)

# lines2 = [[n  if num_str] for line in lines]

# _p1 = p1()
# _p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
