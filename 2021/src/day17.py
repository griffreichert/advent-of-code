import utils


lines = utils.read_list(__file__, as_str=True)
(x1, x2), (y2, y1) = tuple(
    tuple(int(i) for i in chunk[2:].split("..")) for chunk in lines[0][13:].split(", ")
)


def get_triangular_num(x):
    tn = 1
    t = 1
    while tn < x:
        t += 1
        tn += t
    return t


min_vx = get_triangular_num(x1)


def launch_probe(vx, vy):
    """returns the horizontal calibration of the probe at the bottom depth (-1 miss left, 0 hit, 1 miss right)"""
    x, y = vx, vy
    while x <= x2 and y >= y2:
        if x1 <= x <= x2 and y1 >= y >= y2:
            return 0
        vx = max(vx - 1, 0)
        vy -= 1
        x += vx
        y += vy
    return -1 if x < x1 else 1


max_y = 0
horz_calibration = 1
for vy in range(1, 1_000):
    horz_calibration = launch_probe(min_vx, vy)
    if horz_calibration == 0:
        max_y = vy

_p1 = (max_y**2 + max_y) // 2


"""
y between [y2, max_y]
x between [min_x, x2]

"""
velocities = set()

for vy in range(y2, max_y + 1):
    for vx in range(min_vx, x2 + 1):
        horz_calibration = launch_probe(vx, vy)
        if horz_calibration == 0:
            velocities.add((vx, vy))

_p2 = len(velocities)


print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
