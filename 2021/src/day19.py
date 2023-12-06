import utils
from collections import deque, defaultdict, Counter
from heapq import heappop, heappush
import numpy as np
import re
from pprint import pprint
import itertools
import math

with open(f"../data/day19.txt", "r") as f:
    scanners = [
        [
            tuple(int(i) for i in s.split(","))
            for s in scanner.split("\n")
            if "---" not in s
        ]
        for scanner in f.read().strip().split("\n\n")
    ]
# print(scanners)


def get_rotations(pos):
    x, y, z = pos
    return [
        (x, y, z),
        (x, z, -y),
        (x, -y, -z),
        (x, -z, y),
        (-x, -y, z),
        (-x, z, y),
        (-x, y, -z),
        (-x, -z, -y),
        (y, z, x),
        (y, x, -z),
        (y, -z, -x),
        (y, -x, z),
        (-y, -z, x),
        (-y, x, z),
        (-y, z, -x),
        (-y, -x, -z),
        (z, x, y),
        (z, y, -x),
        (z, -x, -y),
        (z, -y, x),
        (-z, -x, y),
        (-z, y, x),
        (-z, x, -y),
        (-z, -y, -x),
    ]


NUM_OVERLAPPING_BEACONS = 12
SIMILARITY_THRESHOLD = math.comb(12, 2)


def calculate_vector(a, b):
    # given two vectors (tuples),
    return tuple(sorted(abs(k) for k in utils.sub_tuples(a, b)))


# set to store "true" position of all beacons
# initialise it as relative to the first scanner
global_locs = set(b for b in scanners[0])

# keep track of the scanners that have been aligned
aligned_scanners = set(0)

search_queue = []

# def p1():

# calculate the set of beacon  vectors within each scanner
all_vectors = []
for beacons in scanners:
    beacon_vectors = set()
    for a, b in itertools.combinations(beacons, 2):
        beacon_vectors.add(calculate_vector(a, b))
    all_vectors.append(beacon_vectors)

for i, j in itertools.combinations(range(len(all_vectors)), r=2):
    similar_beacon_vectors = all_vectors[i].intersection(all_vectors[j])
    # if we want to match 12 beacons, we need 12 choose 2 combinations of offset vectors
    if len(similar_beacon_vectors) >= SIMILARITY_THRESHOLD:
        print("similar")
        # bruteus forceus
        # rotate the beacons so it aligns with the previous one

    # print("combo")
    # print(similar_beacon_vectorslen()))


_p1 = None
_p2 = None

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")

""" wfeng

from functools import lru_cache
from itertools import combinations
from collections import defaultdict

with open("./day_19.in") as fin:
    raw_data = fin.read().strip()
    raw_data = raw_data.split("\n")

"
Game plan:
  - Function that generates all permutations of a set of 3D points (or vectors)
  - Keep track of a relative offsets between scanners
  - Keep track of orientations of scanners

  - Consider all pairs of scanners
      * Find whether we can piece them together
      * If we can, use beacon locations to find offsets and rotations
"

# Parse some input
scanners = []
i = 0
while i < len(raw_data):
    beacons = []
    while i < len(raw_data) and len(raw_data[i]) > 0:
        if "--- scanner" in raw_data[i]:
            i += 1
            continue
        beacons.append(tuple([int(i)
                       for i in raw_data[i].split(",")]))
        i += 1
    scanners.append(tuple(sorted(beacons)))
    i += 1


@lru_cache(None)
def inv(rot):
    a = rotations((1, 2, 3))[rot]
    for inv_rot in range(24):
        if rotations(a)[inv_rot] == (1, 2, 3):
            return inv_rot


@lru_cache(None)
def compose(rot1, rot2):
    a = rotations(rotations((1, 2, 3))[rot1])[rot2]
    for comp_rot in range(24):
        if rotations((1, 2, 3))[comp_rot] == a:
            return comp_rot


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def neg(a):
    return (-a[0], -a[1], -a[2])


def mag(a):
    return a[0]**2 + a[1]**2 + a[2]**2


@lru_cache(None)
def rotations(point):
    # https://i.imgur.com/Ff1vGT9.png
    x, y, z = point
    return [
        (x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y),
        (-x, -y, z), (-x, z, y), (-x, y, -z), (-x, -z, -y),
        (y, z, x), (y, x, -z), (y, -z, -x), (y, -x, z),
        (-y, -z, x), (-y, x, z), (-y, z, -x), (-y, -x, -z),
        (z, x, y), (z, y, -x), (z, -x, -y), (z, -y, x),
        (-z, -x, y), (-z, y, x), (-z, x, -y), (-z, -y, -x)
    ]


def hash(a):
    # Absolute value-ize and sort components
    return tuple(sorted([abs(x) for x in a]))


def offset_set(beacons):
    # Return set of relative offsets between beacons
    res = set()
    for a, b in combinations(beacons, r=2):
        res.add(sub(a, b))
    return res


@lru_cache(None)
def distance_set(beacons):
    # beacons should be a tuple
    return set([hash(v) for v in offset_set(beacons)])


def might_have_overlap(a, b):
    # Determine whether two scanners might overlap based on hashes only
    # (misleading naming)
    if len(set.intersection(distance_set(a), distance_set(b))) >= 66:
        return True
    return False


def orient(a, b, base_index, rots):
    # base_index is the index of some beacon in _a_ that can be aligned
    # rotations is 2 possible rotations (inverses of each other) that we should try
    a_set = set(a)

    for rot in rots:
        other_beacons = tuple([rotations(beacon)[rot] for beacon in b])
        for other_base in other_beacons:
            translate = sub(a[base_index], other_base)
            other_beacons_translated = set(
                [add(beacon, translate) for beacon in other_beacons])

            # See if there's a line-up
            if len(set.intersection(a_set, other_beacons_translated)) >= 12:
                # Woo
                return translate, rot

    return None


def have_overlap(a, b):
    # Actually determine if scanners have overlap
    if not might_have_overlap(a, b):
        return False

    for i, j in combinations(range(len(a)), r=2):
        for k, m in combinations(range(len(b)), r=2):
            da = sub(a[i], a[j])
            db = sub(b[k], b[m])
            if not hash(da) == hash(db):
                continue

            # Determine the rotation and offset
            rots = []

            rot_db = rotations(db)
            for r in range(24):
                if rot_db[r] == da:
                    rots.append(r)
                    break

            # Try mirrored
            db = neg(db)
            rot_db = rotations(db)
            for r in range(24):
                if rot_db[r] == da:
                    rots.append(r)
                    break

            if len(rots) == 0:
                continue

            return orient(a, b, i, rots)

    return False


adj = defaultdict(list)
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        x = have_overlap(scanners[i], scanners[j])
        if x:
            adj[i].append((j, x[0], x[1]))
            adj[j].append((i, rotations(neg(x[0]))[inv(x[1])], inv(x[1])))


# DFS time!
beacons = set()

stack = [(0, (0, 0, 0), 0)]
visited = set()
while len(stack) > 0:
    node, trans, rot = stack.pop()

    if node in visited:
        continue
    visited.add(node)

    # Add these beacons
    cur_beacons = [add(rotations(beacon)[rot], trans)
                   for beacon in scanners[node]]

    for b in cur_beacons:
        beacons.add(b)

    for nbr in adj[node]:
        if nbr[0] in visited:
            continue
        new_trans = add(trans, rotations(nbr[1])[rot])
        new_rot = compose(nbr[2], rot)
        stack.append((nbr[0], new_trans, new_rot))

print(len(beacons))

"""


""" nthistle
from collections import defaultdict, Counter
import regex
import itertools
import numpy as np

mats = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 0, -1], [0, 1, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, -1, 0]], [[0, -1, 0], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]], [[0, 1, 0], [1, 0, 0], [0, 0, -1]], [[0, 0, -1], [1, 0, 0], [0, -1, 0]], [[-1, 0, 0], [0, -1, 0], [0, 0, 1]], [[-1, 0, 0], [0, 0, -1], [0, -1, 0]], [[-1, 0, 0], [0, 1, 0], [0, 0, -1]], [[-1, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], [[0, 0, 1], [-1, 0, 0], [0, -1, 0]], [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], [[0, 0, -1], [-1, 0, 0], [0, 1, 0]], [[0, 0, -1], [0, 1, 0], [1, 0, 0]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[0, 0, 1], [0, -1, 0], [1, 0, 0]], [[0, -1, 0], [0, 0, -1], [1, 0, 0]], [[0, 0, -1], [0, -1, 0], [-1, 0, 0]], [[0, -1, 0], [0, 0, 1], [-1, 0, 0]], [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], [[0, 1, 0], [0, 0, -1], [-1, 0, 0]]]
mats = [np.array(x) for x in mats]

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n\n")


sc = []
for slines in s:
    lines = slines.split("\n")
    locs = set()
    for line in lines[1:]:
        locs.add(eval(line))
    locs = np.array([x for x in locs])
    sc.append((nums(lines[0])[0], locs))

true_locs = set()
for b in sc[0][1]:
    true_locs.add(tuple(b))

scanner_locs = set()

# beacons are the transposed beacons
def align(idx,beacons,already_aligned,depth=0):
    global true_locs
    #print("called at idx =",idx)
    # make a set of your current beacons
    beacon1set = set(tuple(b) for b in beacons)
    # iterate over all scanners
    for i in range(len(sc)):
        # ignore scanners you've aligned 
        if i not in already_aligned:
            print("-"*depth+"trying to align",idx,"with",i)
            bigbreak = False
            # iterate over the possible orientations 
            for orient in range(24):
                # 
                beacon2s = sc[i][1] @ mats[orient]
                for b1x,b1y,b1z in beacons:
                    for b2x,b2y,b2z in beacon2s[:18]:
                        sx,sy,sz = b1x-b2x,b1y-b2y,b1z-b2z
                        beacon2s_tr = beacon2s + np.array([[sx,sy,sz]])
                        intersect = 0
                        for b in beacon2s_tr:
                            if tuple(b) in beacon1set:
                                intersect += 1
                        if intersect >= 12:
                            print("ALIGNING! i =",i)
                            for b in beacon2s_tr:
                                true_locs.add(tuple(b))
                            already_aligned.add(i)
                            align(i,beacon2s_tr,already_aligned,depth+1)
                            bigbreak = True
                            break
                    if bigbreak:
                        break
                if bigbreak:
                    break


align(0,sc[0][1],{0})
print(len(true_locs))

scanner_locs = []
scanner_locs.append((0,0,0))

for i in range(len(sc)):
    print("locating scanner",i)
    for orient in range(24):
        beacon2s = sc[i][1] @ mats[orient]
        for b1x,b1y,b1z in true_locs:
            b2x,b2y,b2z = beacon2s[0]
            sx,sy,sz = b1x-b2x,b1y-b2y,b1z-b2z
            beacon2s_tr = beacon2s + np.array([[sx,sy,sz]])
            intersect = 0
            for b in beacon2s_tr:
                if tuple(b) in true_locs:
                    intersect += 1
            if intersect == beacon2s.shape[0]:
                scanner_locs.append((sx,sy,sz))
                print(intersect)
                print(sx,sy,sz)
                print(orient)
            

md = 0
for i in range(len(scanner_locs)):
    for j in range(i+1,len(scanner_locs)):
        d = sum(abs(scanner_locs[i][k]-scanner_locs[j][k]) for k in range(3))
        md = max(d, md)
print(md)
                
            

        


"""
