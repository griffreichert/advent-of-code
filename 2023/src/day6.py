import utils
import numpy as np


lines = utils.read_list(__file__, as_str=True)

races = [
    (t, d)
    for t, d in zip(
        utils.find_int(lines[0].split(":")[-1], all=True),
        utils.find_int(lines[1].split(":")[-1], all=True),
    )
]


def ways_to_win_races(races):
    ways_to_win = []
    # every second youp hold the button the boat will go 1 mps faster
    for time, total_distance in races:
        button_times = np.array(range(1, time))
        velocities = -button_times + time
        race_res = button_times * velocities
        ways_to_win.append(len(np.where(race_res > total_distance)[0]))
    return utils.list_product(ways_to_win)


_p1 = ways_to_win_races(races)

races = [
    (
        utils.list_to_int([t for t, _ in races]),
        utils.list_to_int([d for _, d in races]),
    )
]

_p2 = ways_to_win_races(races)


print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
