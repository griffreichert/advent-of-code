with open('../data/day25.txt') as f:
    lines = f.read().strip().split('\n')

def clean(s):
    if s == '-':
        return -1
    elif s == '=':
        return -2
    return eval(s)

snafu = [[clean(c) for c in line] for line in lines]

def snafu_to_dec(s):
    dec = 0
    for n in s:
        dec *= 5
        dec += n
    return dec

def dec_to_snafu(d):
    # get list of base 5 numbers from the decimal number
    b5_list = []
    b5 = d
    while b5:
        b5_list.insert(0, b5%5)
        b5 //= 5
    b5_list.insert(0, 0)
    while any(s > 2 for s in b5_list):
        for i, s in enumerate(b5_list):
            if s > 2:
                # increment the digit to the left by one, decrease current digit by 5
                b5_list[i] -= 5
                b5_list[i-1] += 1
    res = ''.join([str(s) if s >= 0 else '-' if s == -1 else '=' for s in b5_list])
    # remove leading 0
    if res[0] == '0':
        res = res[1:]
    print(d)
    print(res)

decimal = [snafu_to_dec(s) for s in snafu]
dec_to_snafu(sum(decimal))