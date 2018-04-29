# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 4

# Part I
def find_combos(orders):
    combos = {'dumpling': 0, 'hamburger': 0, 'ramen': 0, 'salad': 0, 'soda': 0, 'water': 0}
    for I in orders: combos[I] += 1
    return [min(combos['dumpling'], combos['ramen']), min(combos['hamburger'], combos['soda']),
            min(combos['salad'], combos['water'])]


# Part II
def blackjack_dice(dice):
    next_die, play_one, play_two, a_rolled, b_rolled = 0, 0, 0, True, True
    while next_die < len(dice):
        die1 = dice[next_die]
        die2 = dice[next_die + 1]
        if play_one >= 16:
            a_rolled = False
            b_rolled = True
        if play_two >= 16:
            b_rolled = False
            a_rolled = True
        if play_one > 21:
            return [2, play_two]
        if play_two > 21:
            return [1, play_one]
        if play_one == 21:
            return [1, play_one]
        if play_two == 21:
            return [2, play_two]
        if play_one >= 16 and play_two >= 16:
            break
        if a_rolled is True:
            play_one += die1 + die2
            a_rolled = False
            b_rolled = True
            next_die += 2
            continue
        if b_rolled is True:
            play_two += die1 + die2
            a_rolled = True
            b_rolled = False
            next_die += 2
            continue
        next_die += 2
    if play_one > play_two:
        return [1, play_one]
    elif play_one < play_two:
        return [2, play_two]
    return [0, 0]
