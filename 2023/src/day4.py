import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint


lines = utils.read_list(__file__, as_str=True)


cards = {
    utils.find_int(line.split(":")[0]): tuple(
        utils.find_int(part, all=True) for part in line.split(":")[-1].split("|")
    )
    for line in lines
}


def p1():
    num_winners = [sum(n in winners for n in nums) for nums, winners in cards.values()]
    return sum(2 ** (nw - 1) for nw in num_winners if nw > 0)


def p2():
    card_counts = {i + 1: 1 for i in range(len(cards))}
    for i, (nums, winners) in cards.items():
        num_winners = sum(n in winners for n in nums)
        if num_winners > 0:
            for j in range(i + 1, min(len(cards), i + num_winners) + 1):
                card_counts[j] += card_counts[i]
    return sum(card_counts.values())


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
