import pandas as pd

# read in the data
# spaces = pd.read_csv('example.txt', names=['elf1', 'elf2'])
spaces = pd.read_csv('../data/day4.txt', names=['elf1', 'elf2'])

# get the low and high ranges for each elf
spaces['e1_low'] = spaces['elf1'].apply(lambda x: int(x.split('-')[0]))
spaces['e1_high'] = spaces['elf1'].apply(lambda x: int(x.split('-')[1]))
spaces['e2_low'] = spaces['elf2'].apply(lambda x: int(x.split('-')[0]))
spaces['e2_high'] = spaces['elf2'].apply(lambda x: int(x.split('-')[1]))

# method to determine if a range is contained in another range
def is_contained(row):
    if (row.e1_low >= row.e2_low and row.e1_high <= row.e2_high) or (row.e2_low >= row.e1_low and row.e2_high <= row.e1_high):
        return 1
    return 0
    
spaces['contained'] = spaces.apply(lambda row: is_contained(row), axis=1)

print(f'\nPart 1\nnumber of pairs where one range contains the other: {spaces.contained.sum()}')

# method to determine if a range overlaps another range
def count_overlap(row):
    for i in list(range(row.e1_low, row.e1_high + 1)):
        if i in list(range(row.e2_low, row.e2_high + 1)):
            return 1
    return 0

spaces['overlap'] = spaces.apply(lambda row: count_overlap(row), axis=1)

print(f'\nPart 2\nnumber of pairs where one range overlaps the other: {spaces.overlap.sum()}')
