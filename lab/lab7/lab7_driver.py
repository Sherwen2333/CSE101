import sys

student_file = 'lab7.py'

lines = open(student_file).readlines()
lines = [line.strip() for line in lines]
lines = [line if not line.startswith('#') else '' for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'input' in lines[i]:
        print(f'Line {i} of {student_file} contains an input() statement. You must delete this line.')
        code_clean = False
    if 'exit' in lines[i] or 'sys.exit' in lines[i]:
        print(f'Line {i} of {student_file} contains an exit() statement. You must delete this line.')
        code_clean = False
    if 'while ' in lines[i] or 'for ' in lines[i]:
        print(f'Line {i} of {student_file} contains a loop statement.')
        print('You must use recursive algorithms ONLY for this assignment.')
        code_clean = False

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()

part_counts = [0] * 2
test_counts = [10, 10]

from lab7 import *

# Testing Part I
args = [
    [2596],
    [641],
    [3153],
    [3148],
    [3012],
    [779],
    [308],
    [3722],
    [3448],
    [1171],
]
expected_return_values = [
    147,
    52,
    62,
    62,
    23,
    60,
    25,
    39,
    44,
    58,
]

print("############ Testing Part I ############")
for a, e in zip(args, expected_return_values):
    print('Testing rec_hailstone_length() with n = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = rec_hailstone_length(*a)
    print('Actual:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part II
args = [
    [['1sprinkler', '4window', '3pipe', '1window', '4pipe', '3pipe', '2window'], (7, 4, 6)],
    [['3pipe', '3sprinkler', '4pipe', '3pipe', '1pipe', '3window', '2sprinkler', '4sprinkler', '3pipe', '4window'], (3, 6, 6)],
    [['2pipe', '4pipe', '4pipe', '3sprinkler', '4window', '1sprinkler'], (6, 4, 5)],
    [['3window', '4window', '1sprinkler', '4window', '2pipe'], (7, 4, 8)],
    [['4window', '3window', '2pipe', '2sprinkler', '3sprinkler', '2pipe'], (8, 6, 4)],
    [['1window', '3pipe', '3window', '3window', '3sprinkler', '2sprinkler'], (7, 7, 7)],
    [['2sprinkler', '2window', '3sprinkler', '2pipe', '4sprinkler', '2sprinkler'], (3, 5, 3)],
    [['4window', '3sprinkler', '2pipe', '2pipe', '3window', '2window', '4sprinkler', '1window', '2sprinkler', '1pipe'], (7, 2, 7)],
    [['3sprinkler', '2sprinkler', '2pipe', '1pipe', '1pipe', '2pipe', '1pipe', '4pipe', '1pipe', '3sprinkler'], (2, 3, 5)],
    [['4pipe', '4sprinkler', '4sprinkler', '3window', '4pipe', '4pipe', '3pipe', '1window', '4pipe', '2window'], (3, 7, 7)],
]
expected_return_values = [
    104,
    138,
    96,
    66,
    94,
    105,
    49,
    118,
    64,
    155,
]

print("############ Testing Part II ############")
for a, e in zip(args, expected_return_values):
    print('Testing rec_work_cost() with:\n   work_orders = {}\n   hourly_costs = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = rec_work_cost(*a)
    print('Actual:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')
