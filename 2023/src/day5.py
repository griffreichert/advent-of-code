import utils


lines = utils.read_list(__file__, as_str=True)
seeds = utils.find_int(lines[0], all=True)

with open(f"../data/day5.txt", "r") as f:
    maps = [
        [tuple(utils.find_int(m_line, all=True)) for m_line in m_chunk.split("\n")[1:]]
        for m_chunk in f.read().strip().split("\n\n")[1:]
    ]


def grow_seed(s):
    for m in maps:
        for dest, source, n in m:
            if source <= s < source + n:
                s = dest + (s - source)
                break
    return s


def grow_seed_range(seed_start, srange_len):
    # iterate over the ranges and split them into chunks of new ranges
    ranges = [(seed_start, seed_start + srange_len)]

    def map_ranges(ranges: list, range_maps: list):
        mapped = []
        for mapping_dest, mapping, n in range_maps:
            mapping_end = mapping + n
            remaining_ranges = []
            while ranges:
                r_start, r_end = ranges.pop()
                before = r_start, min(r_end, mapping)
                intersect = max(r_start, mapping), min(r_end, mapping_end)
                after = max(r_start, mapping_end), r_end
                # if the ranges are not empty add them
                if before[0] < before[1]:
                    remaining_ranges.append(before)
                if intersect[0] < intersect[1]:
                    # map the intersection
                    istart, iend = intersect
                    mapping_offset = mapping_dest - mapping
                    mapped.append((istart + mapping_offset, iend + mapping_offset))
                    # done with this, dont need to look at it again in future iters
                if after[0] < after[1]:
                    remaining_ranges.append(after)
            ranges = remaining_ranges
        return mapped + remaining_ranges

    for m in maps:
        ranges = map_ranges(ranges, m)

    return min(min(range) for range in ranges)


def p1():
    return min(grow_seed(s) for s in seeds)


def p2():
    new_seeds = [tuple(seeds[i : i + 2]) for i in range(0, len(seeds), 2)]
    return min(grow_seed_range(s_start, s_len) for s_start, s_len in new_seeds)


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
