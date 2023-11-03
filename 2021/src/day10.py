import utils

lines = utils.read_list(__file__, as_str=True)

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
lefts = ["(", "{", "[", "<"]
rights = [")", "}", "]", ">"]
combined = ["()", "{}", "[]", "<>"]

matches = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

points_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def p1():
    res = 0
    for line in lines:
        # iteratively pop any combined patterns until none remain
        modified = True
        while modified:
            prev_len = len(line)
            for pattern in combined:
                # remove the pattern
                line = line.replace(pattern, "")
            # if we've removed something, keep going
            modified = len(line) != prev_len
        # error line if any right symbols remain
        if any(r in line for r in rights):
            for x in line:
                # find the first character that violates the rules, add it's point value
                if x in rights:
                    res += points[x]
                    break
    return res


def p2():
    # list to hold incomplete scores
    incomplete_scores = []
    for line in lines:
        # iteratively pop any combined patterns until none remain
        modified = True
        while modified:
            prev_len = len(line)
            for pattern in combined:
                # remove the pattern
                line = line.replace(pattern, "")
            # if we've removed something, keep going
            modified = len(line) != prev_len

        # incomplete lines only have left characters in them
        if not any(r in line for r in rights):
            res = 0
            # remember to reverse the characters you add
            for x in reversed(line):
                # different scoring, multiply by 5 then add the value of the matching character
                res *= 5
                res += points_2[matches[x]]
            incomplete_scores.append(res)
    # take the median score
    return utils.median(incomplete_scores)


_p1 = p1()
_p2 = p2()

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
