from collections import deque
import utils

lines = utils.read_list(__file__, as_str=True)
fish = utils.find_int(lines[0], all=True)


def lanternfish_populaiton_growth(time):
    # use a deque to count the number of fish with each ammount of time left
    population = deque([0 for _ in range(9)])
    for f in fish:
        population[f] += 1
    
    for _ in range(time):
        # adult fish reproduce every 6 days (move them to 7 bc we shift)
        population[7] += population[0]
        # shift the population (decrease time) and have fish at 0 move to 8 (offspring)
        population.rotate(-1)
    return sum(population)


print("p1")
print(lanternfish_populaiton_growth(80))
print("p2")
print(lanternfish_populaiton_growth(256))