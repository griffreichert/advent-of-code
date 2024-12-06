import re

import utils

text = utils.read_lines(__file__, parse_ints=False)[0]


def p1():
    matches = re.findall(r"mul\((\d+),(\d+)\)", text)
    return sum(int(a) * int(b) for a, b in matches)


def p2():
    cleaned = re.sub(r"don\'t\(\).*?do\(\)", "", text).rsplit("don't()", 1)[0]
    matches = re.findall(r"mul\((\d+),(\d+)\)", cleaned)
    return sum(int(a) * int(b) for a, b in matches)


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
