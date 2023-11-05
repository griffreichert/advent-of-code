import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint


lines = utils.read_list(__file__, as_str=True)

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

packet = "".join(hex_to_binary[char] for char in lines[0])

# first three bits are the packet header
# next three bits are the packet type id
# packets with id 4 are a literal
# literals come in groups of 4 bits with 1 bit preceeding them (the last group is prefaced with a 0, others with a 1)


def p1(packet):
    packet_versions = []
    packets = deque([packet])
    while packets:
        p = packets.popleft()
        try:
            version = p[:3]
            id_type = p[3:6]
        except:
            break
        # literal
        if id_type == "100":
            i = 6
            while True:
                pass
        # operator
        else:
            # type length id
            type_len_id = p[6]
            if type_len_id == "1":
                pass
            else:
                pass

        packet_versions.append(int(version, 2))

    return sum(packet_versions)


def p2():
    res = 0
    return res


_p1 = p1(packet)
_p2 = p2()

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
