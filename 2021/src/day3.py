import utils
from copy import deepcopy

lines = utils.read_list(__file__, as_str=True)




def p1(lines):
    n = len(lines)
    new_lines = [[] for _ in range(len(lines[0]))]
    for line in lines:
        for i, char in enumerate(line):
            new_lines[i].append(int(char))
    gamma = int(''.join(str(round(sum(register)/n)) for register in new_lines), 2)
    epsil = int(''.join(str(1 - round(sum(register)/n)) for register in new_lines), 2)
    return gamma * epsil

def p2(lines):
    n = len(lines[0])
    
    def filter_lines(lines, i, target):
        return [line for line in lines if line[i]==target]
    
    def most_common_in_pos(lines, i):
        c1 = sum(1 if line[i] == '1' else 0 for line in lines)
        c0 = len(lines) - c1
        return '1' if c1 >= c0 else '0'
    
    def get_o2(lines):
        pos = 0 
        while len(lines) > 1:
            lines = filter_lines(lines, pos, most_common_in_pos(lines, pos))
            pos += 1
        return int(lines[0], 2)
    
    def get_co2(lines):
        pos = 0 
        while len(lines) > 1:
            lines = filter_lines(lines, pos, str(1 - int(most_common_in_pos(lines, pos))))
            pos += 1
        return int(lines[0], 2)
    
    o2 = get_o2(lines)
    co2 = get_co2(lines)
    return o2 * co2

print("p1")
print(p1(lines))
print("p2")
print(p2(lines))
