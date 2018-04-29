from lab3 import *
import sys

student_file = 'lab3.py'

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

# Testing Part I
args = [
    ['kBfmR@93&BvS'],
    ['zs4*ia0QFer5'],
    ['@YIc!8pY14nM'],
    ['4utb8Z'],
    ['7P8VC508@e2LTh'],
    ['2YERJ3pKPZ9qU7nxR1'],
    ['B4MP22EY4L6'],
    ['8um^3bv2gtq3U6wW8O9f'],
    ['Z9NYRvfHx%S0^P'],
    ['IA8mH!R'],
]
expected = [
    ['BRBS', 'kfmv', '93'],
    ['QF', 'zsiaer', '405'],
    ['YIYM', 'cpn', '814'],
    ['Z', 'utb', '48'],
    ['PVCLT', 'eh', '785082'],
    ['YERJKPZUR', 'pqnx', '23971'],
    ['BMPEYL', '', '42246'],
    ['UWO', 'umbvgtqwf', '8323689'],
    ['ZNYRHSP', 'vfx', '90'],
    ['IAHR', 'm', '8'],
]

print("########## Testing Part I ##########")
for a, e in zip(args, expected):
    print('Testing summation() with st = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(sanitize(*a)))
print('########################################')
print()

# Testing Part II
args = [
    [[13, 1, 1, 1], ['plate', 'soda', 'soda', 'plate', 'plate', 'pizza']],
    [[10, 1, 2, 1], ['soda', 'pizza', 'pizza', 'soda', 'plate', 'plate', 'cup', 'soda', 'cup', 'cup', 'plate', 'soda', 'cup']],
    [[20, 2, 2, 3], ['soda', 'soda', 'soda', 'plate', 'cup', 'pizza', 'soda', 'soda', 'soda', 'plate', 'soda', 'pizza', 'plate']],
    [[13, 2, 4, 2], ['cup', 'plate', 'plate', 'soda', 'cup', 'soda', 'plate', 'soda', 'plate', 'soda', 'plate', 'cup', 'pizza', 'plate', 'cup', 'soda', 'cup', 'cup']],
    [[11, 2, 3, 2], ['plate', 'plate', 'plate', 'cup', 'soda', 'pizza', 'plate', 'plate', 'soda', 'pizza', 'pizza']],
    [[12, 2, 2, 3], ['soda', 'cup', 'cup', 'soda', 'soda', 'cup', 'cup', 'cup']],
    [[18, 1, 4, 2], ['soda', 'cup', 'plate', 'soda', 'cup', 'soda', 'soda', 'soda', 'plate', 'cup', 'soda', 'pizza', 'plate', 'cup', 'soda', 'soda', 'cup', 'plate', 'soda', 'pizza']],
    [[16, 2, 4, 1], ['soda', 'soda', 'cup', 'cup', 'cup', 'plate', 'pizza', 'pizza', 'plate', 'pizza', 'plate', 'cup', 'cup', 'soda']],
    [[19, 1, 1, 1], ['soda', 'pizza', 'cup', 'plate', 'soda', 'cup', 'plate', 'cup', 'pizza', 'soda', 'soda', 'soda', 'pizza', 'cup']],
    [[19, 2, 3, 3], ['soda', 'plate', 'cup', 'cup', 'soda', 'cup', 'plate', 'soda', 'soda', 'soda', 'soda', 'pizza', 'plate', 'soda', 'pizza', 'soda', 'plate', 'plate', 'cup']],
]
expected = [
    18,
    30.6,
    60.587999999999994,
    58.2,
    43.2,
    19,
    66.20400000000001,
    58.400000000000006,
    54.08,
    74.772,
]

print("########## Testing Part II ##########")
for a, e in zip(args, expected):
    print('Testing party() with prices = {}, shopping_list = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(party(*a)))
print('########################################')
print()

# Testing Part III
args = [
    [16],
    [3],
    [44],
    [7],
    [2],
    [4],
    [24],
    [37],
    [13],
    [32],
]
expected = [
    'High school',
    'Too young for school',
    'College',
    'Elementary school',
    'Too young for school',
    'Too young for school',
    'College',
    'College',
    'Middle school',
    'College',
]

print("########## Testing Part III ##########")
for a, e in zip(args, expected):
    print('Testing school_dilemma() with age = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(school_dilemma(*a)))
print('########################################')
print()