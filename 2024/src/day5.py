from collections import defaultdict

import utils

lines = utils.read_lines(__file__, parse_ints=True)
i = lines.index([])
page_rules = lines[:i]
page_lists = lines[i + 1 :]
page_maps = [{page: i for i, page in enumerate(pages)} for pages in page_lists]
rule_maps = defaultdict(set)
for first, second in page_rules:
    rule_maps[first].add(second)


def p1():
    good_pages = []
    for page_map, page_list in zip(page_maps, page_lists):
        for first, second in page_rules:
            if first in page_map and second in page_map:
                if page_map[first] > page_map[second]:
                    break
        else:
            good_pages.append(page_list)
    return sum(page_list[len(page_list) // 2] for page_list in good_pages)


def p2():
    bad_page_idx = []
    for p, page_map in enumerate(page_maps):
        for first, second in page_rules:
            if first in page_map and second in page_map:
                if page_map[first] > page_map[second]:
                    bad_page_idx.append(p)
                    break

    # sort page lists
    sorted_pages = []
    for p in bad_page_idx:
        pages = page_lists[p]
        i = 0
        while i < len(pages) - 1:
            check = pages[i]
            for j in range(i + 1, len(pages)):
                cur = pages[j]
                if cur in rule_maps[check]:
                    # swap
                    pages[i] = cur
                    pages[j] = check
                    i -= 1
                    break
            i += 1
        sorted_pages.append(pages)

    # sum midpoints
    return sum(pages[len(pages) // 2] for pages in sorted_pages)


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}\n")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
