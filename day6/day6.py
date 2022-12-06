
# with open('example.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f:
        signal = list(line)
        for i in range(4, len(signal)):
            if len(set(signal[i-4:i]))==4:
                print(f'\nPart 1\n{i}')
                break
        for i in range(14, len(signal)):
            if len(set(signal[i-14:i]))==14:
                print(f'\nPart 2\n{i}')
                break