import utils
from tqdm import tqdm

lines = utils.read_lines(__file__, parse_ints=True)


def p1():
    res = 0
    for line in lines:
        ans = line[0]
        heap = [line[1:]]
        while heap:
            cur = heap.pop(0)
            if cur[0] > ans:
                continue
            if len(cur) == 1:
                if ans == cur[0]:
                    res += ans
                    break
                continue
            a = cur.pop(0)
            b = cur.pop(0)
            heap.append([a + b] + cur)
            heap.append([a * b] + cur)
    return res


def p2():
    res = 0
    for line in tqdm(lines):
        ans = line[0]
        heap = [line[1:]]
        while heap:
            cur = heap.pop(0)
            if cur[0] > ans:
                continue
            if len(cur) == 1:
                if ans == cur[0]:
                    res += ans
                    break
                continue
            a = cur.pop(0)
            b = cur.pop(0)
            heap.append([a + b] + cur)
            heap.append([a * b] + cur)
            heap.append([utils.list_to_int([a, b])] + cur)
    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
