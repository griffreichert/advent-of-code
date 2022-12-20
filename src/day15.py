
from pprint import pprint

# with open('../data/day15.txt') as f:
with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n')
    
    
def parse(line):
    sensor_str, beacon_str = line.split(':')
    s_i = eval(sensor_str.split('y=')[1].split(',')[0])
    s_j = eval(sensor_str.split('x=')[1].split(',')[0])
    b_i = eval(beacon_str.split('y=')[1].split(',')[0])
    b_j = eval(beacon_str.split('x=')[1].split(',')[0])
    return (s_i, s_j, b_i, b_j)

sensors = [parse(line) for line in lines]
pprint(sensors)