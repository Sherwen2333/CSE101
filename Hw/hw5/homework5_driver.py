import sys

student_file = 'homework5.py'

lines = open(student_file).readlines()
lines = [line.strip() for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'input' in lines[i] and not lines[i].startswith('#'):
        print('Line {} of {} contains an input() statement. You must delete this line.'. \
              format(i, student_file))
        code_clean = False
    if 'exit' in lines[i] or 'sys.exit' in lines[i]:
        print('Line {} of {} contains an exit() statement. You must delete this line.'. \
              format(i, student_file))

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()

from homework5 import *

part_counts = [0] * 6
test_counts = [1, 2, 20, 3, 20, 20]

# Testing Part I
expected_return_values = [
'[2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♣, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♠, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦, A♦, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♥]'
]

print("############ Testing Part I ############")
for e in expected_return_values:
    print('Testing create_deck():')
    print('Expected Return Value: {}'.format(e))
    actual = str(create_deck())
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part II
args = [
    [[Card(0,0), Card(1,0), Card(2,0), Card(3,0), Card(4,0), Card(5,0), Card(6,0), Card(7,0), Card(8,0), Card(9,0), Card(10,0), Card(11,0), Card(12,0), Card(0,1), Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1), Card(6,1), Card(7,1), Card(8,1), Card(9,1), Card(10,1), Card(11,1), Card(12,1), Card(0,2), Card(1,2), Card(2,2), Card(3,2), Card(4,2), Card(5,2), Card(6,2), Card(7,2), Card(8,2), Card(9,2), Card(10,2), Card(11,2), Card(12,2), Card(0,3), Card(1,3), Card(2,3), Card(3,3), Card(4,3), Card(5,3), Card(6,3), Card(7,3), Card(8,3), Card(9,3), Card(10,3), Card(11,3), Card(12,3)]],
    [[Card(12,0), Card(4,0), Card(9,2), Card(11,3), Card(10,2), Card(10,0), Card(2,2), Card(1,2), Card(11,0), Card(6,1), Card(2,1), Card(8,3), Card(0,1), Card(8,2), Card(4,2), Card(12,1), Card(5,1), Card(7,0), Card(4,3), Card(8,0), Card(5,2), Card(5,3), Card(0,3), Card(3,3), Card(3,0), Card(12,2), Card(1,3), Card(12,3), Card(0,0), Card(1,1), Card(8,1), Card(3,1), Card(6,2), Card(10,3), Card(11,2), Card(7,2), Card(9,1), Card(7,3), Card(2,3), Card(1,0), Card(4,1), Card(9,0), Card(0,2), Card(3,2), Card(2,0), Card(6,0), Card(10,1), Card(9,3), Card(11,1), Card(6,3), Card(5,0), Card(7,1)]],
]
expected_return_values = [
    '(Player(1,0,[2♣, 4♣, 6♣, 8♣, 10♣, Q♣, A♣, 3♠, 5♠, 7♠, 9♠, J♠, K♠, 2♦, 4♦, 6♦, 8♦, 10♦, Q♦, A♦, 3♥, 5♥, 7♥, 9♥, J♥, K♥]), Player(2,0,[3♣, 5♣, 7♣, 9♣, J♣, K♣, 2♠, 4♠, 6♠, 8♠, 10♠, Q♠, A♠, 3♦, 5♦, 7♦, 9♦, J♦, K♦, 2♥, 4♥, 6♥, 8♥, 10♥, Q♥, A♥]))',
    '(Player(1,0,[A♣, J♦, Q♦, 4♦, K♣, 4♠, 2♠, 6♦, 7♠, 6♥, 7♦, 2♥, 5♣, 3♥, 2♣, 10♠, 8♦, K♦, J♠, 4♥, 6♠, 2♦, 4♣, Q♠, K♠, 7♣]), Player(2,0,[6♣, K♥, Q♣, 3♦, 8♠, 10♥, 10♦, A♠, 9♣, 10♣, 7♥, 5♥, A♦, A♥, 3♠, 5♠, Q♥, 9♦, 9♥, 3♣, J♣, 5♦, 8♣, J♥, 8♥, 9♠]))',
]

print("############ Testing Part II ############")
for a, e in zip(args, expected_return_values):
    print('Testing deal_cards() with deck = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = str(deal_cards(*a))
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part III
args = [
    [Player(1,0,[Card(12,0), Card(9,2), Card(10,2), Card(2,2), Card(11,0), Card(2,1), Card(0,1), Card(4,2), Card(5,1), Card(4,3), Card(5,2), Card(0,3), Card(3,0), Card(1,3), Card(0,0), Card(8,1), Card(6,2), Card(11,2), Card(9,1), Card(2,3), Card(4,1)]), Player(2,0,[Card(4,0), Card(11,3), Card(10,0), Card(1,2), Card(6,1), Card(8,3), Card(8,2), Card(12,1), Card(7,0), Card(8,0), Card(5,3), Card(3,3), Card(12,2), Card(12,3), Card(1,1), Card(3,1), Card(10,3), Card(7,2), Card(7,3), Card(1,0), Card(9,0)])],
    [Player(1,0,[Card(11,3), Card(1,1), Card(3,3), Card(0,0), Card(1,2), Card(5,2), Card(0,3), Card(0,1), Card(7,0)]), Player(2,0,[Card(12,0), Card(10,2), Card(8,3), Card(2,0), Card(8,0), Card(3,0), Card(9,2), Card(0,2), Card(5,1)])],
    [Player(1,0,[Card(3,3), Card(5,1), Card(6,2), Card(0,0), Card(1,2), Card(2,2), Card(8,0), Card(7,0), Card(4,0), Card(9,0), Card(11,3), Card(6,0), Card(10,2), Card(1,3), Card(7,1), Card(5,0), Card(7,2), Card(4,2), Card(11,2)]), Player(2,0,[Card(3,1), Card(2,0), Card(0,3), Card(11,1), Card(12,2), Card(12,3), Card(4,1), Card(4,3), Card(12,1), Card(1,0), Card(3,0), Card(9,1), Card(12,0), Card(3,2), Card(0,2), Card(8,2), Card(2,1), Card(9,2), Card(11,0)])],
    [Player(1,0,[Card(4,1), Card(4,0), Card(3,1), Card(2,3), Card(9,2), Card(10,3)]), Player(2,0,[Card(12,2), Card(4,3), Card(7,1), Card(9,0), Card(0,1), Card(10,1)])],
    [Player(1,0,[Card(6,2), Card(1,1), Card(5,1), Card(12,3), Card(8,3), Card(3,3), Card(3,1), Card(4,2), Card(1,3), Card(7,2), Card(9,0), Card(6,0), Card(6,3)]), Player(2,0,[Card(2,0), Card(1,2), Card(1,0), Card(8,2), Card(4,1), Card(8,0), Card(11,3), Card(3,2), Card(5,2), Card(10,2), Card(0,3), Card(11,0), Card(9,2)])],
    [Player(1,0,[Card(9,1), Card(7,2), Card(0,3), Card(12,1), Card(6,3), Card(2,1)]), Player(2,0,[Card(11,0), Card(7,0), Card(10,2), Card(1,0), Card(6,1), Card(9,0)])],
    [Player(1,0,[Card(1,2), Card(5,3), Card(3,2), Card(3,3), Card(6,1), Card(2,1), Card(4,0), Card(1,1), Card(0,2), Card(5,0), Card(8,1)]), Player(2,0,[Card(12,0), Card(2,2), Card(7,2), Card(11,1), Card(9,2), Card(0,1), Card(7,3), Card(4,1), Card(10,1), Card(10,0), Card(1,3)])],
    [Player(1,0,[Card(8,3), Card(3,2), Card(6,0), Card(3,1), Card(6,2), Card(11,1), Card(12,0), Card(0,1), Card(12,3), Card(7,0), Card(0,0), Card(1,0)]), Player(2,0,[Card(9,0), Card(1,2), Card(10,0), Card(5,1), Card(0,3), Card(4,2), Card(1,3), Card(6,1), Card(9,2), Card(1,1), Card(2,0), Card(10,1)])],
    [Player(1,0,[Card(11,1), Card(0,3), Card(6,2), Card(5,0)]), Player(2,0,[Card(3,2), Card(7,1), Card(5,2), Card(4,2)])],
    [Player(1,0,[Card(2,3), Card(1,3), Card(12,3), Card(12,2), Card(0,1), Card(10,1), Card(3,3), Card(9,0)]), Player(2,0,[Card(10,3), Card(7,3), Card(3,0), Card(2,2), Card(11,0), Card(10,2), Card(1,0), Card(6,1)])],
    [Player(1,0,[Card(10,3), Card(2,1), Card(1,0), Card(1,2), Card(5,3), Card(10,0)]), Player(2,0,[Card(1,3), Card(3,2), Card(0,2), Card(11,0), Card(10,1), Card(2,3)])],
    [Player(1,0,[Card(12,0), Card(10,1), Card(10,2), Card(11,3), Card(8,3), Card(9,0), Card(1,0), Card(0,2), Card(6,0), Card(10,3), Card(10,0), Card(5,2), Card(11,0), Card(4,0), Card(6,2), Card(7,3)]), Player(2,0,[Card(12,1), Card(5,1), Card(0,3), Card(3,2), Card(8,1), Card(6,1), Card(2,0), Card(11,2), Card(8,0), Card(5,3), Card(4,3), Card(4,2), Card(11,1), Card(12,3), Card(5,0), Card(0,0)])],
    [Player(1,0,[Card(5,1), Card(2,0), Card(5,3), Card(7,3), Card(0,1), Card(7,1), Card(4,0), Card(11,2), Card(9,0), Card(6,2), Card(11,1), Card(1,1), Card(6,3), Card(4,1), Card(7,2), Card(8,1), Card(6,0)]), Player(2,0,[Card(10,0), Card(12,0), Card(10,1), Card(1,0), Card(1,3), Card(5,0), Card(6,1), Card(8,2), Card(0,0), Card(10,2), Card(12,2), Card(8,0), Card(10,3), Card(5,2), Card(7,0), Card(9,1), Card(2,3)])],
    [Player(1,0,[Card(0,2), Card(10,3), Card(9,2), Card(4,1), Card(11,1), Card(0,1), Card(5,3), Card(10,1)]), Player(2,0,[Card(10,2), Card(5,1), Card(3,0), Card(9,3), Card(4,3), Card(11,3), Card(4,0), Card(6,1)])],
    [Player(1,0,[Card(9,0), Card(9,3), Card(7,1), Card(8,1), Card(0,1), Card(4,1), Card(7,2), Card(4,0), Card(2,0), Card(10,3), Card(5,1), Card(8,3), Card(8,0), Card(0,2), Card(5,0), Card(10,1), Card(11,2)]), Player(2,0,[Card(0,3), Card(12,0), Card(12,1), Card(12,3), Card(7,3), Card(11,1), Card(3,2), Card(10,0), Card(2,3), Card(3,0), Card(10,2), Card(3,1), Card(6,2), Card(6,0), Card(1,1), Card(4,3), Card(1,2)])],
    [Player(1,0,[Card(1,2)]), Player(2,0,[Card(10,0)])],
    [Player(1,0,[Card(6,3), Card(3,1), Card(4,1), Card(9,3), Card(10,3), Card(8,1), Card(9,1), Card(1,2), Card(1,3), Card(5,0), Card(8,0), Card(7,2), Card(2,3), Card(11,0), Card(8,3), Card(3,2)]), Player(2,0,[Card(3,3), Card(0,0), Card(6,2), Card(3,0), Card(9,2), Card(12,0), Card(7,3), Card(1,1), Card(5,2), Card(11,3), Card(2,0), Card(4,0), Card(9,0), Card(7,1), Card(10,2), Card(12,2)])],
    [Player(1,0,[Card(1,0), Card(9,2), Card(5,1), Card(4,3), Card(9,3), Card(3,0), Card(11,0), Card(6,1), Card(12,0), Card(6,2), Card(10,2), Card(1,2), Card(9,0)]), Player(2,0,[Card(12,1), Card(12,3), Card(8,0), Card(7,0), Card(3,2), Card(0,0), Card(10,1), Card(9,1), Card(8,3), Card(0,3), Card(3,3), Card(8,1), Card(6,3)])],
    [Player(1,0,[Card(1,0), Card(12,0), Card(0,0), Card(6,0), Card(4,0), Card(5,0), Card(3,0), Card(7,0), Card(8,0), Card(9,0), Card(10,0), Card(11,0), Card(2,0), Card(0,1), Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1), Card(6,1), Card(7,1), Card(8,1), Card(9,1), Card(10,1), Card(11,1), Card(12,1)]), Player(2,0,[Card(1,2), Card(12,2), Card(0,2), Card(3,2), Card(4,2), Card(5,2), Card(6,2), Card(7,2), Card(8,2), Card(9,2), Card(10,2), Card(11,2), Card(2,2), Card(0,3), Card(1,3), Card(2,3), Card(3,3), Card(4,3), Card(5,3), Card(6,3), Card(7,3), Card(8,3), Card(9,3), Card(10,3), Card(11,3), Card(12,3)])],
    [Player(1,0,[Card(0,0), Card(1,0), Card(2,0), Card(3,0), Card(4,0), Card(5,0), Card(6,0), Card(7,0), Card(8,0), Card(9,0), Card(10,0), Card(11,0), Card(12,0), Card(0,1), Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1), Card(6,1), Card(7,1), Card(8,1), Card(9,1), Card(10,1), Card(11,1), Card(12,1)]), Player(2,0,[Card(0,2), Card(1,2), Card(2,2), Card(3,2), Card(4,2), Card(5,2), Card(6,2), Card(7,2), Card(8,2), Card(9,2), Card(10,2), Card(11,2), Card(12,2), Card(0,3), Card(1,3), Card(2,3), Card(3,3), Card(4,3), Card(5,3), Card(6,3), Card(7,3), Card(8,3), Card(9,3), Card(10,3), Card(11,3), Card(12,3)])],
]
expected_return_values = [
    (1, 2),
    (2, 2),
    (1, 4),
    (2, 2),
    (1, 2),
    (2, 2),
    (2, 2),
    (2, 2),
    (1, 2),
    (2, 2),
    (1, 2),
    (1, 4),
    (2, 2),
    (2, 2),
    (1, 2),
    (2, 2),
    (1, 2),
    (2, 2),
    (1, 8),
    (0, 0),
]

print("############ Testing Part III ############")
for a, e in zip(args, expected_return_values):
    print('Testing play_normal_round() with\n\tplayer1 = {}\n\tplayer2 = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = play_normal_round(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[2] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part IV
args = [
    [Player(1,8,[Card(3,0), Card(1,3), Card(0,0), Card(8,1), Card(6,2), Card(11,2), Card(9,1), Card(2,3), Card(4,1), Card(0,2), Card(2,0), Card(10,1), Card(11,1), Card(5,0)]), Player(2,16,[Card(12,2), Card(12,3), Card(1,1), Card(3,1), Card(10,3), Card(7,2), Card(7,3), Card(1,0), Card(9,0), Card(3,2), Card(6,0), Card(9,3), Card(6,3), Card(7,1)])],
    [Player(1,10,[Card(3,3), Card(8,0), Card(4,1), Card(0,0), Card(4,3), Card(12,2), Card(10,1), Card(8,3), Card(11,1), Card(2,3), Card(3,2), Card(6,2), Card(9,2), Card(0,1), Card(11,2), Card(2,2), Card(9,1), Card(3,1)]), Player(2,6,[Card(6,3), Card(12,0), Card(10,2), Card(12,3), Card(0,3), Card(9,0), Card(8,1), Card(7,3), Card(0,2), Card(7,2), Card(3,0), Card(1,0), Card(4,0), Card(5,3), Card(7,1), Card(5,2), Card(11,0), Card(7,0)])],
    [Player(1,0,[Card(5,1), Card(5,0), Card(7,0), Card(6,0), Card(4,0), Card(1,0), Card(3,0), Card(2,0), Card(8,0), Card(9,0), Card(10,0), Card(11,0), Card(12,0), Card(0,1), Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(0,0), Card(6,1), Card(7,1), Card(8,1), Card(9,1), Card(10,1), Card(11,1), Card(12,1)]), Player(2,0,[Card(5,3), Card(5,2), Card(7,2), Card(3,2), Card(4,2), Card(1,2), Card(6,2), Card(2,2), Card(8,2), Card(9,2), Card(10,2), Card(11,2), Card(12,2), Card(0,3), Card(1,3), Card(2,3), Card(3,3), Card(4,3), Card(0,2), Card(6,3), Card(7,3), Card(8,3), Card(9,3), Card(10,3), Card(11,3), Card(12,3)])],
]
expected_return_values = [
    2,
    1,
    0,
]
print("############ Testing Part IV ############")
for a, e in zip(args, expected_return_values):
    print('Testing check_game_winner() with\n\tplayer1 = {}\n\tplayer2 = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = check_game_winner(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[3] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part V
args = [
    [Player(1,0,[Card(12,0), Card(9,2), Card(10,2), Card(2,2), Card(11,0), Card(2,1), Card(0,1), Card(4,2), Card(5,1), Card(4,3), Card(5,2), Card(0,3), Card(3,0), Card(1,3), Card(0,0), Card(8,1), Card(6,2), Card(11,2), Card(9,1), Card(2,3), Card(4,1)]), Player(2,0,[Card(4,0), Card(11,3), Card(10,0), Card(1,2), Card(6,1), Card(8,3), Card(8,2), Card(12,1), Card(7,0), Card(8,0), Card(5,3), Card(3,3), Card(12,2), Card(12,3), Card(1,1), Card(3,1), Card(10,3), Card(7,2), Card(7,3), Card(1,0), Card(9,0)])],
    [Player(1,0,[Card(11,3), Card(1,1), Card(3,3), Card(0,0), Card(1,2), Card(5,2), Card(0,3), Card(0,1), Card(7,0)]), Player(2,0,[Card(12,0), Card(10,2), Card(8,3), Card(2,0), Card(8,0), Card(3,0), Card(9,2), Card(0,2), Card(5,1)])],
    [Player(1,0,[Card(3,3), Card(5,1), Card(6,2), Card(0,0), Card(1,2), Card(2,2), Card(8,0), Card(7,0), Card(4,0), Card(9,0), Card(11,3), Card(6,0), Card(10,2), Card(1,3), Card(7,1), Card(5,0), Card(7,2), Card(4,2), Card(11,2)]), Player(2,0,[Card(3,1), Card(2,0), Card(0,3), Card(11,1), Card(12,2), Card(12,3), Card(4,1), Card(4,3), Card(12,1), Card(1,0), Card(3,0), Card(9,1), Card(12,0), Card(3,2), Card(0,2), Card(8,2), Card(2,1), Card(9,2), Card(11,0)])],
    [Player(1,0,[Card(4,1), Card(4,0), Card(3,1), Card(2,3), Card(9,2), Card(10,3)]), Player(2,0,[Card(12,2), Card(4,3), Card(7,1), Card(9,0), Card(0,1), Card(10,1)])],
    [Player(1,0,[Card(6,2), Card(1,1), Card(5,1), Card(12,3), Card(8,3), Card(3,3), Card(3,1), Card(4,2), Card(1,3), Card(7,2), Card(9,0), Card(6,0), Card(6,3)]), Player(2,0,[Card(2,0), Card(1,2), Card(1,0), Card(8,2), Card(4,1), Card(8,0), Card(11,3), Card(3,2), Card(5,2), Card(10,2), Card(0,3), Card(11,0), Card(9,2)])],
    [Player(1,0,[Card(9,1), Card(7,2), Card(0,3), Card(12,1), Card(6,3), Card(2,1)]), Player(2,0,[Card(11,0), Card(7,0), Card(10,2), Card(1,0), Card(6,1), Card(9,0)])],
    [Player(1,0,[Card(1,2), Card(5,3), Card(3,2), Card(3,3), Card(6,1), Card(2,1), Card(4,0), Card(1,1), Card(0,2), Card(5,0), Card(8,1)]), Player(2,0,[Card(12,0), Card(2,2), Card(7,2), Card(11,1), Card(9,2), Card(0,1), Card(7,3), Card(4,1), Card(10,1), Card(10,0), Card(1,3)])],
    [Player(1,0,[Card(8,3), Card(3,2), Card(6,0), Card(3,1), Card(6,2), Card(11,1), Card(12,0), Card(0,1), Card(12,3), Card(7,0), Card(0,0), Card(1,0)]), Player(2,0,[Card(9,0), Card(1,2), Card(10,0), Card(5,1), Card(0,3), Card(4,2), Card(1,3), Card(6,1), Card(9,2), Card(1,1), Card(2,0), Card(10,1)])],
    [Player(1,0,[Card(11,1), Card(0,3), Card(6,2), Card(5,0)]), Player(2,0,[Card(3,2), Card(7,1), Card(5,2), Card(4,2)])],
    [Player(1,0,[Card(2,3), Card(1,3), Card(12,3), Card(12,2), Card(0,1), Card(10,1), Card(3,3), Card(9,0)]), Player(2,0,[Card(10,3), Card(7,3), Card(3,0), Card(2,2), Card(11,0), Card(10,2), Card(1,0), Card(6,1)])],
    [Player(1,0,[Card(10,3), Card(2,1), Card(1,0), Card(1,2), Card(5,3), Card(10,0)]), Player(2,0,[Card(1,3), Card(3,2), Card(0,2), Card(11,0), Card(10,1), Card(2,3)])],
    [Player(1,0,[Card(12,0), Card(10,1), Card(10,2), Card(11,3), Card(8,3), Card(9,0), Card(1,0), Card(0,2), Card(6,0), Card(10,3), Card(10,0), Card(5,2), Card(11,0), Card(4,0), Card(6,2), Card(7,3)]), Player(2,0,[Card(12,1), Card(5,1), Card(0,3), Card(3,2), Card(8,1), Card(6,1), Card(2,0), Card(11,2), Card(8,0), Card(5,3), Card(4,3), Card(4,2), Card(11,1), Card(12,3), Card(5,0), Card(0,0)])],
    [Player(1,0,[Card(5,1), Card(2,0), Card(5,3), Card(7,3), Card(0,1), Card(7,1), Card(4,0), Card(11,2), Card(9,0), Card(6,2), Card(11,1), Card(1,1), Card(6,3), Card(4,1), Card(7,2), Card(8,1), Card(6,0)]), Player(2,0,[Card(10,0), Card(12,0), Card(10,1), Card(1,0), Card(1,3), Card(5,0), Card(6,1), Card(8,2), Card(0,0), Card(10,2), Card(12,2), Card(8,0), Card(10,3), Card(5,2), Card(7,0), Card(9,1), Card(2,3)])],
    [Player(1,0,[Card(0,2), Card(10,3), Card(9,2), Card(4,1), Card(11,1), Card(0,1), Card(5,3), Card(10,1)]), Player(2,0,[Card(10,2), Card(5,1), Card(3,0), Card(9,3), Card(4,3), Card(11,3), Card(4,0), Card(6,1)])],
    [Player(1,0,[Card(9,0), Card(9,3), Card(7,1), Card(8,1), Card(0,1), Card(4,1), Card(7,2), Card(4,0), Card(2,0), Card(10,3), Card(5,1), Card(8,3), Card(8,0), Card(0,2), Card(5,0), Card(10,1), Card(11,2)]), Player(2,0,[Card(0,3), Card(12,0), Card(12,1), Card(12,3), Card(7,3), Card(11,1), Card(3,2), Card(10,0), Card(2,3), Card(3,0), Card(10,2), Card(3,1), Card(6,2), Card(6,0), Card(1,1), Card(4,3), Card(1,2)])],
    [Player(1,0,[Card(1,2)]), Player(2,0,[Card(10,0)])],
    [Player(1,0,[Card(6,3), Card(3,1), Card(4,1), Card(9,3), Card(10,3), Card(8,1), Card(9,1), Card(1,2), Card(1,3), Card(5,0), Card(8,0), Card(7,2), Card(2,3), Card(11,0), Card(8,3), Card(3,2)]), Player(2,0,[Card(3,3), Card(0,0), Card(6,2), Card(3,0), Card(9,2), Card(12,0), Card(7,3), Card(1,1), Card(5,2), Card(11,3), Card(2,0), Card(4,0), Card(9,0), Card(7,1), Card(10,2), Card(12,2)])],
    [Player(1,0,[Card(1,0), Card(9,2), Card(5,1), Card(4,3), Card(9,3), Card(3,0), Card(11,0), Card(6,1), Card(12,0), Card(6,2), Card(10,2), Card(1,2), Card(9,0)]), Player(2,0,[Card(12,1), Card(12,3), Card(8,0), Card(7,0), Card(3,2), Card(0,0), Card(10,1), Card(9,1), Card(8,3), Card(0,3), Card(3,3), Card(8,1), Card(6,3)])],
    [Player(1,0,[Card(0,0), Card(2,0), Card(4,0), Card(6,2), Card(8,0), Card(10,0), Card(12,0), Card(1,1), Card(3,1), Card(5,1), Card(7,1), Card(9,1), Card(11,1), Card(0,2), Card(2,2), Card(4,2), Card(6,0), Card(8,2), Card(10,2), Card(12,2), Card(1,3), Card(3,3), Card(5,3), Card(7,3), Card(9,3), Card(11,3)]), Player(2,0,[Card(1,0), Card(3,0), Card(5,0), Card(7,0), Card(9,0), Card(11,0), Card(0,1), Card(2,1), Card(4,1), Card(6,1), Card(8,1), Card(10,1), Card(12,1), Card(1,2), Card(3,2), Card(5,2), Card(7,2), Card(9,2), Card(11,2), Card(0,3), Card(2,3), Card(4,3), Card(6,3), Card(8,3), Card(10,3), Card(12,3)])],
    [Player(1,0,[Card(0,0), Card(1,0), Card(2,0), Card(3,0), Card(4,0), Card(5,0), Card(6,0), Card(7,0), Card(8,0), Card(9,0), Card(10,0), Card(11,0), Card(12,0), Card(0,1), Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1), Card(6,1), Card(7,1), Card(8,1), Card(9,1), Card(10,1), Card(11,1), Card(12,1)]), Player(2,0,[Card(0,2), Card(1,2), Card(2,2), Card(3,2), Card(4,2), Card(5,2), Card(6,2), Card(7,2), Card(8,2), Card(9,2), Card(10,2), Card(11,2), Card(12,2), Card(0,3), Card(1,3), Card(2,3), Card(3,3), Card(4,3), Card(5,3), Card(6,3), Card(7,3), Card(8,3), Card(9,3), Card(10,3), Card(11,3), Card(12,3)])],
]
expected_return_values = [
    (2, 4),
    (2, 2),
    (1, 2),
    (1, 2),
    (1, 2),
    (1, 2),
    (1, 2),
    (2, 2),
    (1, 2),
    (2, 6),
    (1, 4),
    (2, 2),
    (1, 2),
    (1, 4),
    (1, 2),
    (1, 2),
    (1, 4),
    (2, 2),
    (1, 8),
    (2, 2),
]
print("############ Testing Part V ############")
for a, e in zip(args, expected_return_values):
    print('Testing play_with_suits() with\n\tplayer1 = {}\n\tplayer2 = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = play_with_suits(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[4] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part VI
args = [
    [Player(1,0,[Card(12,0), Card(9,2), Card(10,2), Card(2,2), Card(11,0), Card(2,1), Card(0,1), Card(4,2), Card(5,1), Card(4,3), Card(5,2), Card(0,3), Card(3,0), Card(1,3), Card(0,0), Card(8,1), Card(6,2), Card(11,2), Card(9,1), Card(2,3), Card(4,1)]), Player(2,0,[Card(4,0), Card(11,3), Card(10,0), Card(1,2), Card(6,1), Card(8,3), Card(8,2), Card(12,1), Card(7,0), Card(8,0), Card(5,3), Card(3,3), Card(12,2), Card(12,3), Card(1,1), Card(3,1)])],
    [Player(1,0,[Card(12,3), Card(1,1), Card(3,3), Card(0,0), Card(1,2), Card(5,2), Card(0,3), Card(0,1), Card(7,0)]), Player(2,0,[Card(12,0), Card(10,2), Card(6,3), Card(2,0), Card(8,0), Card(3,0), Card(9,2), Card(0,2), Card(5,1), Card(3,1)])],
    [Player(1,0,[Card(7,0), Card(6,1), Card(3,1), Card(0,0), Card(1,2), Card(0,3), Card(8,0), Card(7,2), Card(1,3), Card(2,2), Card(1,0), Card(3,0), Card(9,1), Card(12,0), Card(6,2), Card(0,2), Card(10,2), Card(2,1), Card(9,2)]), Player(2,0,[Card(4,1), Card(2,0), Card(5,0), Card(12,1), Card(11,1), Card(3,2)])],
    [Player(1,0,[Card(4,0), Card(9,0), Card(0,3)]), Player(2,0,[Card(1,3), Card(10,2), Card(0,1), Card(5,3), Card(8,3), Card(11,2), Card(12,1), Card(3,1), Card(7,1), Card(11,1), Card(7,2), Card(5,2), Card(10,0), Card(4,3), Card(6,1), Card(8,2), Card(1,2), Card(6,3), Card(12,2), Card(11,3), Card(1,1), Card(12,0), Card(10,3), Card(6,2), Card(6,0)])],
    [Player(1,0,[Card(1,1), Card(5,0), Card(11,1), Card(7,0), Card(2,0), Card(4,0), Card(3,3), Card(10,2), Card(6,1), Card(3,1), Card(1,3), Card(0,0), Card(4,2), Card(2,3), Card(11,0), Card(6,3), Card(9,0), Card(0,1), Card(7,3), Card(12,1)]), Player(2,0,[Card(8,2), Card(5,2), Card(7,2), Card(9,2), Card(5,1), Card(3,2), Card(8,0), Card(0,3), Card(1,2), Card(4,1), Card(8,1), Card(11,3), Card(6,2), Card(6,0), Card(9,3), Card(1,0), Card(0,2), Card(10,1), Card(8,3), Card(7,1), Card(12,0), Card(3,0)])],
    [Player(1,0,[Card(2,1)]), Player(2,0,[Card(3,2), Card(9,0), Card(5,2), Card(3,0), Card(6,1), Card(10,0), Card(12,3), Card(5,1), Card(12,2), Card(9,1), Card(6,3), Card(11,3), Card(0,3), Card(6,0), Card(7,1), Card(12,1), Card(7,3), Card(10,2), Card(4,0), Card(6,2)])],
    [Player(1,0,[Card(11,3), Card(4,0), Card(6,1), Card(9,3), Card(0,1), Card(9,2), Card(1,1), Card(5,2), Card(11,2), Card(4,1), Card(1,2), Card(10,0), Card(4,3), Card(11,1), Card(9,1), Card(6,0), Card(5,0), Card(1,3), Card(6,3), Card(11,0), Card(0,0), Card(12,2)]), Player(2,0,[Card(10,1), Card(3,3), Card(0,3), Card(8,1), Card(2,2), Card(12,0), Card(2,1), Card(7,2), Card(3,2), Card(4,2), Card(6,2), Card(0,2), Card(12,3), Card(9,0), Card(7,1)])],
    [Player(1,0,[Card(10,1), Card(4,2), Card(10,3), Card(5,1), Card(12,3), Card(10,2), Card(11,0), Card(7,2), Card(1,0), Card(7,3), Card(1,3), Card(11,1), Card(0,3), Card(1,1), Card(5,3), Card(8,1), Card(0,0), Card(11,3), Card(3,3)]), Player(2,0,[Card(4,3), Card(12,0), Card(3,2), Card(6,1), Card(0,1), Card(2,3), Card(2,0), Card(4,1), Card(1,2), Card(12,2), Card(3,1), Card(8,3), Card(9,2), Card(6,2), Card(7,0), Card(6,3), Card(5,0), Card(10,0)])],
    [Player(1,0,[Card(10,1), Card(3,3), Card(1,3), Card(2,2), Card(5,0), Card(4,0), Card(2,3), Card(12,2), Card(3,0), Card(6,1), Card(10,0), Card(1,0), Card(12,0), Card(9,0), Card(6,2), Card(1,1), Card(7,0), Card(7,3)]), Player(2,0,[Card(10,2), Card(4,3), Card(1,2), Card(0,2), Card(12,3), Card(11,0), Card(6,0), Card(8,3), Card(12,1), Card(4,2), Card(9,3), Card(5,3), Card(7,2), Card(6,3), Card(5,2), Card(3,2), Card(0,3), Card(11,2), Card(7,1), Card(11,3), Card(11,1)])],
    [Player(1,0,[Card(9,0), Card(1,0), Card(12,3), Card(9,1), Card(7,0), Card(1,3), Card(7,3), Card(4,0), Card(1,2), Card(10,1), Card(8,2), Card(1,1), Card(6,1), Card(4,2), Card(8,1), Card(12,1), Card(0,1), Card(12,0), Card(7,2), Card(10,3)]), Player(2,0,[Card(11,3), Card(11,1), Card(3,3), Card(6,0), Card(0,3), Card(0,2), Card(9,3), Card(8,3), Card(3,0), Card(2,3), Card(5,0), Card(6,3), Card(12,2), Card(7,1), Card(2,1), Card(11,0), Card(2,2), Card(10,2), Card(0,0), Card(8,0), Card(9,2), Card(10,0)])],
    [Player(1,0,[Card(7,2), Card(0,0), Card(10,3), Card(1,2), Card(4,3), Card(0,2), Card(6,0), Card(8,3), Card(2,2), Card(4,1), Card(5,2), Card(8,1)]), Player(2,0,[Card(5,0), Card(1,1), Card(1,0), Card(9,2), Card(5,3), Card(1,3), Card(9,0), Card(3,1), Card(10,1), Card(9,1), Card(7,1), Card(2,3), Card(6,3), Card(8,0), Card(0,1)])],
    [Player(1,0,[Card(11,0), Card(5,0), Card(9,2), Card(8,2), Card(12,0), Card(11,2), Card(4,3), Card(5,2), Card(7,3), Card(5,3), Card(12,1), Card(4,2), Card(3,0), Card(0,3)]), Player(2,0,[Card(3,1), Card(2,0), Card(6,3), Card(8,0), Card(12,2), Card(10,2), Card(8,3), Card(11,1), Card(0,2), Card(10,3), Card(9,3), Card(6,2), Card(4,0)])],
    [Player(1,0,[Card(5,0), Card(4,2), Card(11,2), Card(5,2), Card(7,1), Card(4,3), Card(10,0), Card(6,1), Card(1,3), Card(2,0), Card(6,3), Card(12,3), Card(2,2), Card(7,3), Card(5,3), Card(8,2), Card(0,1)]), Player(2,0,[Card(10,1), Card(4,0), Card(1,0), Card(6,2), Card(4,1), Card(9,3), Card(11,1), Card(12,0), Card(8,3), Card(3,3), Card(8,1), Card(5,1), Card(8,0), Card(7,0), Card(9,0), Card(0,0), Card(10,2), Card(0,3), Card(3,1)])],
    [Player(1,0,[Card(12,2), Card(9,0), Card(4,1), Card(5,0), Card(12,3), Card(7,2), Card(8,3), Card(0,3), Card(9,2), Card(11,2), Card(10,1), Card(2,1), Card(11,3), Card(2,0), Card(8,2), Card(6,1), Card(1,3), Card(4,3)]), Player(2,0,[Card(12,1), Card(7,3), Card(6,0), Card(0,2), Card(2,3), Card(10,2), Card(7,0), Card(0,1), Card(12,0), Card(10,0), Card(9,3), Card(6,3), Card(10,3), Card(3,3), Card(3,2), Card(4,2), Card(4,0), Card(5,1), Card(3,0), Card(11,1), Card(3,1), Card(5,2)])],
    [Player(1,0,[Card(6,0), Card(11,2), Card(7,2), Card(1,3), Card(12,0), Card(8,0), Card(2,3), Card(5,3), Card(10,1), Card(3,0), Card(4,0), Card(4,1), Card(12,1), Card(10,0), Card(10,3), Card(3,3), Card(1,0), Card(6,2), Card(0,1), Card(3,2), Card(7,3), Card(5,2), Card(11,3), Card(6,1), Card(11,0), Card(8,3)]), Player(2,0,[Card(7,1), Card(12,2), Card(0,2), Card(2,1), Card(1,1), Card(12,3), Card(8,2), Card(8,1), Card(5,1), Card(11,1), Card(5,0), Card(4,3), Card(9,0), Card(2,0), Card(6,3), Card(0,3), Card(0,0), Card(3,1), Card(9,3), Card(7,0)])],
    [Player(1,0,[Card(9,2), Card(6,1), Card(8,1), Card(10,0), Card(7,0), Card(8,2), Card(9,1), Card(12,1), Card(4,2), Card(4,3)]), Player(2,0,[Card(6,0), Card(10,3), Card(0,2), Card(1,2), Card(0,1), Card(2,0), Card(11,3), Card(3,1), Card(4,1), Card(8,3), Card(10,2), Card(12,0), Card(5,1), Card(11,2), Card(7,2), Card(12,2), Card(12,3), Card(6,3), Card(2,3), Card(3,0)])],
    [Player(1,0,[Card(7,2), Card(8,0), Card(6,2), Card(12,0), Card(3,3), Card(1,2)]), Player(2,0,[Card(2,0), Card(6,3), Card(7,1), Card(1,3), Card(10,0), Card(0,0), Card(4,3), Card(10,3), Card(5,2), Card(8,3), Card(0,1), Card(12,3), Card(12,2), Card(3,1), Card(3,2)])],
    [Player(1,0,[Card(9,0), Card(3,2), Card(12,3), Card(7,0), Card(10,2), Card(1,2), Card(9,3), Card(5,3), Card(4,1), Card(5,0), Card(2,0), Card(8,3), Card(1,1), Card(12,1), Card(8,0), Card(6,0), Card(0,3), Card(4,0), Card(6,2)]), Player(2,0,[Card(6,3), Card(9,1), Card(12,2), Card(5,2), Card(1,0), Card(11,3), Card(10,1), Card(0,0), Card(3,3), Card(7,3), Card(2,1), Card(2,2)])],
    [Player(1,0,[Card(3,2)]), Player(2,0,[Card(3,3), Card(4,3)])],
    [Player(1,0,[Card(6,3), Card(8,0)]), Player(2,0,[Card(6,1)])],
]
expected_return_values = [
    (1, 2),
    (2, 5),
    (1, 2),
    (2, 3),
    (1, 5),
    (2, 3),
    (1, 2),
    (1, 2),
    (1, 5),
    (2, 2),
    (1, 2),
    (1, 3),
    (2, 2),
    (1, 4),
    (2, 2),
    (1, 2),
    (2, 3),
    (1, 2),
    (2, 3),
    (0, 0),
]
print("############ Testing Part VI ############")
for a, e in zip(args, expected_return_values):
    print('Testing play_with_scouts() with\n\tplayer1 = {}\n\tplayer2 = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = play_with_scouts(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[5] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')
print(f'Part III: {part_counts[2]}/{test_counts[2]}')
print(f'Part IV:  {part_counts[3]}/{test_counts[3]}')
print(f'Part V:   {part_counts[4]}/{test_counts[4]}')
print(f'Part VI:  {part_counts[5]}/{test_counts[5]}')
