from homework3 import *

import sys

student_file = 'homework3.py'

lines = open(student_file).readlines()
lines = [line.strip() for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'input' in lines[i] and not lines[i].startswith('#'):
        print('Line {} of {} contains an input() statement. You must delete this line.'.\
              format(i, student_file))
        code_clean = False
    if 'exit' in lines[i] or 'sys.exit' in lines[i]:
        print('Line {} of {} contains an exit() statement. You must delete this line.'.\
              format(i, student_file))

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()


part_counts = [0] * 5
test_counts = [10, 10, 20, 10, 10]

# Part I Testing
args = [
    [44, ['eat', 'play']],
    [16, ['play', 'eat', 'work']],
    [27, ['play', 'eat', 'read', 'play', 'read', 'read', 'work', 'read', 'eat', 'eat', 'work', 'work', 'work']],
    [41, ['play', 'work', 'eat', 'play']],
    [23, ['work', 'play', 'eat', 'read', 'work', 'read', 'play']],
    [50, ['read', 'eat', 'eat', 'read', 'work', 'read', 'work']],
    [10, ['eat', 'read', 'work', 'eat', 'read', 'read', 'read', 'work']],
    [38, ['play', 'eat', 'work', 'play', 'eat', 'work', 'read', 'play', 'play', 'work', 'read', 'work']],
    [7, ['work', 'play', 'play', 'read', 'work']],
    [24, ['work', 'play', 'eat']],
]
expected = [
    46,
    12,
    0,
    39,
    6,
    25,
    0,
    13,
    0,
    20,
]

print("########## Testing Part I ##########")
for a, e in zip(args, expected):
    print('Testing frog() with mood = {}, actions = {}:'.format(*a))
    print(f'Expected: {e}')
    actual = frog(*a)
    print(f'Actual:   {actual}')
    if e == actual:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Part II Testing
args = [
    [['D']],
    [['g', 'y', 'o', 'R', 'C', 'l', 's', 'U', 'm', 'q']],
    [['m', 'j']],
    [['H']],
    [['s', 'c', 'P', 'u', 'U', 'I', 'T', 'z', 'R']],
    [['j', 'F', 'Q', 'K', 't', 'i']],
    [['m', 'K', 'x', 'J', 's']],
    [['h', 'i', 'o', 'J', 'x', 'e', 'u', 's']],
    [['a', 'B', 'K', 'm', 'n', 'X', 'j']],
    [['u', 'I', 'a', 'U', 'P', 'c', 'k', 'M', 'R', 'x']],
]
expected = [
    ['_', '<'],
    ['<', 'g', 'y', 'o', 'R', 'C', 'l', 's', 'U', 'm', 'q'],
    ['_', '_', '<'],
    ['<', 'H'],
    ['<', 's', 'c', 'P', 'u', 'U', 'I', 'T', 'z', 'R'],
    ['_', '_', '_', '<', 't', 'i'],
    ['_', '_', '_', '<', 's'],
    ['<', 'h', 'i', 'o', 'J', 'x', 'e', 'u', 's'],
    ['_', '_', '_', '_', '_', '_', '_', '<'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '<'],
]

print("########## Testing Part II ##########")
for a, e in zip(args, expected):
    print('Testing pacman() with line = {}:'.format(*a))
    print(f'Expected: {e}')
    actual = pacman(*a)
    print(f'Actual:   {actual}')
    if e == actual:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Part III Testing
args = [
    ['}'],
    ['[{[[{([[()]{({})}])}]]}]'],
    ['[]{[{[]{}{}{()}]}'],
    ['{{({}[[]([]())])}}'],
    ['[][]{'],
    ['{()[({})()]}'],
    ['[]{({}()(()(){[]()}[))}'],
    ['[]()[{[[]({{}[()]})]}]'],
    ['[[[]{}]'],
    ['({{}()}{}{()}{{[][]}})'],
    ['(){}[][]'],
    ['(([{}]))'],
    ['[]['],
    ['[[([{{}}]})]]'],
    ['[([(()()[{{}}[]{[{]}])])]'],
    ['[)][()]'],
    ['()({}){[)()]}'],
    ['({)[{}]'],
    ['{}]()([][][])'],
    ['[{(){{()}}]'],
]
expected = [
    'error',
    [],
    ['{', '[', '{'],
    [],
    ['{'],
    [],
    ['{', '(', '(', '['],
    [],
    ['['],
    [],
    [],
    [],
    ['['],
    ['[', '[', '('],
    ['[', '(', '[', '(', '[', '{', '[', '{'],
    ['['],
    ['{', '['],
    ['(', '{'],
    'error',
    ['[', '{'],
]

print("########## Testing Part III ##########")
for a, e in zip(args, expected):
    print('Testing brackets() with expr = {}'.format(*a))
    print(f'Expected: {e}')
    actual = brackets(*a)
    print(f'Actual:   {actual}')
    if e == actual:
        print('Correct!')
        part_counts[2] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Part IV Testing
args = [
    [1, 968],
    [15, 853],
    [20, 107],
    [13, 825],
    [8, 700],
    [15, 181],
    [10, 748],
    [6, 205],
    [9, 113],
    [7, 152],
]
expected = [
    [1],
    [11, 68, 69, 70, 75, 384, 416, 424, 426, 452, 453, 454],
    [9, 56, 58, 60, 61],
    [17, 96, 104, 106, 113, 640, 672, 680, 682],
    [3, 20, 21, 128],
    [11, 68, 69, 70, 75],
    [12, 13, 80, 84, 85, 512],
    [5, 32],
    [6, 40, 42],
    [10, 64],
]

print("########## Testing Part IV ##########")
for a, e in zip(args, expected):
    print('Testing siblings() with length = {}, maximum = {}:'.format(*a))
    print(f'Expected: {e}')
    actual = siblings(*a)
    print(f'Actual:   {actual}')
    if e == actual:
        print('Correct!')
        part_counts[3] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Part V Testing
args = [
    [51, 2, 8],
    [33, 2, 2],
    [67, 11, 5],
    [83, 11, 8],
    [59, 15, 4],
    [26, 2, 3],
    [50, 3, 4],
    [84, 11, 2],
    [20, 9, 4],
    [61, 12, 7],
]
expected = [
    [51, 0],
    [33, 0],
    [0, 48],
    [80, 0],
    [0, 62],
    [26, 0],
    [50, 0],
    [0, 87],
    [0, 13],
    [53, 0],
]

print("########## Testing Part V ##########")
for a, e in zip(args, expected):
    print('Testing vampire_hunt() with humans = {}, vampires = {}, hunters = {}:'.format(*a))
    print(f'Expected: {e}')
    actual = vampire_hunt(*a)
    print(f'Actual:   {actual}')
    if e == actual:
        print('Correct!')
        part_counts[4] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')
print(f'Part III: {part_counts[2]}/{test_counts[2]}')
print(f'Part IIV: {part_counts[3]}/{test_counts[3]}')
print(f'Part V:   {part_counts[4]}/{test_counts[4]}')