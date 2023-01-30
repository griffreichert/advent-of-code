import pandas as pd

tournament = pd.read_csv('../data/day2.txt', header=None, names=['raw'])

# attach the choices to the scores of the items
abc_cipher = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors
}

xyx_cipher = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}

tournament['opponent'] = tournament.raw.apply(lambda x: x.split(' ')[0]).map(abc_cipher)
tournament['you'] = tournament.raw.apply(lambda x: x.split(' ')[1]).map(xyx_cipher)

def score_round(row):
    # your score is the result of the match + the score of the item you chose
    return score_helper(row.opponent, row.you) + row.you

# decide if the match is a win, loss or draw
def score_helper(opponent, you):
    # default to loss
    score = 0
    # win
    if opponent < you:
        score = 6
    # edge case: your rock beats opponent's scissors
    if opponent == 3 and you == 1:
        score = 6
    # edge case: opponent's rock beats your scissors
    if opponent == 1 and you == 3:
        score = 0
    # draw
    if opponent == you:
        score = 3
    return score

tournament['score'] = tournament.apply(lambda row: score_round(row), axis=1)

# print(tournament.sample(6))

print('\nPart 1:')
print(f'score: {tournament.score.sum()}')


## part 2

# X means lose 
# Y means draw
# Z means win

xyx_cipher_2 = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6,  # win
}

# find the result you need to get
tournament['need_to'] = tournament.raw.apply(lambda x: x.split(' ')[1]).map(xyx_cipher_2)

# reverse engineer which item gets you the result you would need
def optimal_scoring(row):
    for i in range(1, 4):
        if score_helper(row.opponent, i) == row.need_to:
            # remember to add the score of the item to the result you need to get
            return row.need_to + i
        
tournament['optimal_score'] = tournament.apply(lambda row: optimal_scoring(row), axis=1)

print('\nPart 2:')
# print(tournament.sample(6))
print(f'score: {tournament.optimal_score.sum()}')


            

