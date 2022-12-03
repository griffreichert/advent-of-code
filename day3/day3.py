import pandas as pd

# read in the data
# elves = pd.read_csv('example.txt', names=['backpack'])
elves = pd.read_csv('input.txt', names=['backpack'])

# split the list of chars into halves
elves['compartment1'] = elves['backpack'].apply(lambda x: x[:int(len(x)/2)])
elves['compartment2'] = elves['backpack'].apply(lambda x: x[int(len(x)/2):])

# find the item that is in both halves
def find_item(row):
    for item in row.compartment1:
        if item in row.compartment2:
            return item

elves['item'] = elves.apply(lambda row: find_item(row), axis=1)

# find the priority of that item
# a-z 1-26
# A-Z 27-52
def prioritize(item):
    # use ascii to get ints from numbers
    item_int = ord(item)
    # lowercase go from 97-122 so shift it to 1-26
    if item_int >= 97: 
        return item_int - 96
    # uppercase go from 65-90 so shift it to 27-52
    return item_int - 38

elves['priority'] = elves.item.apply(lambda item: prioritize(item))

# sum up all of the priorities
print(f'\nPart 1\ntotal priority: {elves.priority.sum()}')

# find the unique item that group of three has
group_items = []
for i in range(len(elves)):
    # elves are in groups of 3, so only search every 3 elves starting with the first one
    if (i % 3) == 0:
        # if an item in the elf's backpack is in the backpack of the next two elves, add it to the list of group items then move on to the next group
        for item in elves.iloc[i].backpack:
            if (item in elves.iloc[i+1].backpack) and (item in elves.iloc[i+2].backpack):
                group_items.append(item)
                break

# sum up the priorities
print(f'\nPart 2\ntotal group priorities: {sum([prioritize(item) for item in group_items])}')