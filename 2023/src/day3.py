import utils


lines = utils.read_list(__file__, as_str=True)


def symbol_search(i, j):
    for adj in utils.neighbors:
        ni, nj = utils.add_tuples((i, j), adj)
        if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
            cur = lines[ni][nj]
            if not cur.isdigit() and cur != ".":
                return True
    return False


def gear_search(i, j):
    for adj in utils.neighbors:
        ni, nj = utils.add_tuples((i, j), adj)
        if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
            if lines[ni][nj] == "*":
                return ni, nj
    return None


def p1():
    res = 0
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            cur = line[j]
            if cur.isdigit():
                k = j + 1
                while k < len(line) and line[k].isdigit():
                    k += 1
                num = int(line[j:k])
                if any(symbol_search(i, x) for x in range(j, k)):
                    res += num
                    j = k
            j += 1
    return res


def p2():
    gears_seen = {}
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            cur = line[j]
            if cur.isdigit():
                k = j + 1
                while k < len(line) and line[k].isdigit():
                    k += 1
                num = int(line[j:k])
                for x in range(j, k):
                    gear_pos = gear_search(i, x)
                    if gear_pos is not None:
                        if gear_pos not in gears_seen:
                            gears_seen[gear_pos] = [num]
                        else:
                            gears_seen[gear_pos].append(num)
                        break
                j = k
            j += 1
    return sum(
        utils.list_product(nums) for nums in gears_seen.values() if len(nums) == 2
    )


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
