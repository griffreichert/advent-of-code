import utils

lines = utils.read_lines(__file__)

print("p1")
print(sum(1 for i in range(len(lines) - 1) if lines[i + 1] > lines[i]))
print("p2")
print(sum(1 for i in range(len(lines) - 3) if lines[i + 3] > lines[i]))
