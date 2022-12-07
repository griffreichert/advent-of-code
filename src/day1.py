import itertools

elves = {}
elf_index = 1

with open('../data/day1.txt') as file:
    for line in file:
        if line == '\n':
            elf_index += 1
        else:
            i = line.split('\n')[0]
            if elf_index in elves:
                elves[elf_index] += int(i)  
            else:
                elves[elf_index] = int(i)
                
print('\nPart 1:')
print(f'elf {max(elves, key=elves.get)} is carrying the most calories: {max(elves.values())}')

# part 2: find the total calories carried by the top 3 elves

# sort the dict by values
elves = {k: v for k, v in sorted(elves.items(), key=lambda item: -item[1])}

print('\nPart 2:')
print(f'the calories carried by the top three elves in total is: {sum(itertools.islice(elves.values(), 3))}\n')