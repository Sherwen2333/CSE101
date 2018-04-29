from homework5 import *
import random
import war_classes
print_output = war_classes.print_output = True

# Main program
cards = create_deck()
random.shuffle(cards)
player1, player2 = deal_cards(cards)
round_num = 1

use_scouting_rules = False  # set to False for normal War
use_suits_rules = False     # set to False for normal War

while len(player1._cards) > 0 and len(player2._cards) > 0:
    print('Round #' + str(round_num) + ':')
    if use_scouting_rules:
        result = play_with_scouts(player1, player2)
    elif use_suits_rules:
        result = play_with_suits(player1, player2)
    else:
        result = play_normal_round(player1, player2)
    if result[0] == 1:
        if print_output: print('    Player 1 won the round, scoring', result[1], 'points.')
    elif result[0] == 2:
        if print_output: print('    Player 2 won the round, scoring', result[1], 'points.')
    round_num += 1

if print_output:
    print('Final scores:')
    print('Player 1:', player1._score)
    print('Player 2:', player2._score)
    if check_game_winner(player1, player2) == 1:
        print('Player 1 wins!')
    elif check_game_winner(player1, player2) == 2:
        print('Player 2 wins!')
    else:
        print('Tie game!')

