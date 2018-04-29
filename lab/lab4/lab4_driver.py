from lab4 import *
import sys

student_file = 'lab4.py'

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
    [['dumpling', 'water', 'dumpling', 'dumpling', 'ramen', 'ramen', 'water']],
    [['soda', 'dumpling', 'hamburger', 'hamburger', 'hamburger', 'water', 'dumpling', 'ramen']],
    [['salad', 'soda', 'dumpling', 'hamburger', 'water', 'water', 'soda', 'ramen', 'salad']],
    [['water', 'water', 'soda', 'soda', 'salad', 'dumpling', 'soda', 'dumpling']],
    [['water', 'soda', 'water', 'salad', 'soda', 'hamburger', 'soda', 'hamburger', 'soda', 'salad', 'soda']],
    [['hamburger', 'water', 'ramen', 'salad', 'water', 'soda', 'soda', 'soda', 'ramen', 'salad', 'ramen', 'ramen', 'dumpling', 'ramen', 'hamburger']],
    [['water', 'soda', 'hamburger', 'soda', 'dumpling', 'ramen', 'dumpling', 'hamburger', 'soda', 'soda', 'salad', 'soda', 'salad', 'salad', 'dumpling']],
    [['water', 'ramen', 'dumpling', 'ramen', 'salad', 'dumpling', 'ramen', 'soda', 'ramen', 'dumpling']],
    [['salad', 'ramen', 'salad', 'ramen', 'soda', 'water', 'salad', 'ramen']],
    [['ramen', 'water', 'ramen', 'soda', 'ramen', 'hamburger', 'soda', 'ramen', 'dumpling', 'hamburger']],
]
expected = [
    [2, 0, 0],
    [1, 1, 0],
    [1, 1, 2],
    [0, 0, 1],
    [0, 2, 2],
    [1, 2, 2],
    [1, 2, 1],
    [3, 0, 1],
    [0, 0, 1],
    [1, 2, 0],
]

print("############ Testing Part I ############")
for a, e in zip(args, expected):
    print('Testing find_combos() with orders = {}'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(find_combos(*a)))
print('########################################')
print()

# Testing Part II
args = [
    [[5, 1, 6, 1, 1, 3, 3, 6, 5, 5, 1, 2, 2, 2, 6, 1, 3, 2, 6, 2, 3, 6, 4, 2, 4, 2, 4, 2, 3, 6]],
    [[3, 4, 2, 6, 4, 5, 6, 5, 6, 4, 5, 2, 5, 2, 5, 4, 5, 5, 4, 5, 4, 2, 3, 3, 5, 5, 1, 6, 4, 2]],
    [[3, 3, 2, 6, 5, 2, 5, 1, 3, 1, 2, 5, 5, 4, 5, 4, 4, 1, 6, 6, 3, 1, 3, 4, 1, 3, 5, 3, 1, 5]],
    [[4, 3, 4, 3, 5, 6, 4, 3, 3, 2, 1, 4, 4, 3, 2, 6, 4, 2, 2, 1, 1, 3, 5, 1, 1, 1, 2, 5, 6, 1]],
    [[4, 3, 2, 3, 1, 1, 1, 5, 4, 6, 3, 4, 4, 3, 2, 1, 6, 5, 2, 6, 6, 5, 5, 1, 5, 3, 5, 3, 4, 4]],
    [[4, 1, 1, 4, 4, 3, 2, 5, 6, 3, 2, 3, 3, 1, 3, 3, 5, 3, 3, 1, 6, 5, 1, 4, 6, 2, 2, 4, 4, 3]],
    [[4, 4, 6, 3, 4, 6, 1, 3, 3, 3, 1, 3, 1, 6, 1, 5, 5, 5, 6, 4, 4, 3, 5, 2, 2, 4, 3, 5, 2, 3]],
    [[5, 4, 2, 6, 3, 1, 1, 3, 5, 5, 3, 6, 2, 5, 2, 2, 2, 4, 4, 1, 4, 4, 5, 3, 1, 5, 5, 4, 5, 5]],
    [[1, 2, 4, 2, 2, 4, 6, 3, 4, 6, 2, 2, 5, 4, 3, 3, 2, 1, 1, 3, 6, 3, 4, 6, 3, 5, 2, 2, 2, 2]],
    [[3, 5, 1, 2, 6, 4, 4, 5, 1, 6, 4, 6, 2, 5, 5, 2, 6, 4, 3, 1, 6, 5, 1, 5, 6, 3, 6, 1, 4, 5]],
    [[5, 3, 5, 2, 5, 5, 4, 2, 6, 6, 3, 2, 4, 4, 3, 6, 5, 5, 2, 2, 1, 1, 4, 5, 5, 4, 4, 3, 4, 2]],
    [[1, 1, 3, 1, 5, 1, 6, 4, 1, 6, 5, 1, 2, 6, 4, 2, 6, 5, 4, 6, 1, 5, 3, 4, 1, 3, 6, 3, 2, 3]],
    [[4, 3, 2, 2, 3, 3, 4, 3, 6, 2, 5, 4, 3, 5, 5, 1, 5, 4, 1, 4, 2, 4, 5, 1, 4, 4, 5, 6, 2, 1]],
    [[3, 5, 4, 2, 3, 3, 5, 3, 4, 1, 5, 3, 5, 6, 2, 3, 3, 4, 5, 4, 2, 2, 3, 3, 1, 4, 1, 6, 2, 6]],
    [[2, 5, 6, 4, 2, 1, 6, 5, 2, 4, 3, 5, 6, 4, 5, 1, 3, 3, 4, 3, 5, 3, 1, 4, 6, 4, 2, 1, 6, 2]],
    [[1, 2, 6, 1, 2, 6, 5, 4, 6, 6, 6, 3, 5, 2, 1, 1, 3, 6, 4, 4, 4, 3, 5, 4, 3, 4, 4, 2, 1, 1]],
    [[4, 5, 6, 5, 1, 2, 3, 2, 4, 1, 1, 1, 1, 1, 5, 6, 2, 2, 3, 5, 5, 6, 3, 1, 4, 6, 2, 3, 2, 3]],
    [[5, 1, 1, 4, 4, 1, 2, 5, 5, 1, 4, 4, 1, 3, 2, 1, 4, 4, 1, 5, 2, 3, 6, 5, 6, 3, 3, 6, 5, 2]],
    [[1, 5, 2, 3, 4, 6, 4, 6, 6, 6, 2, 5, 2, 5, 2, 6, 1, 1, 4, 5, 3, 1, 6, 4, 1, 1, 4, 5, 1, 2]],
    [[3, 3, 1, 5, 2, 6, 3, 5, 1, 3, 2, 2, 6, 2, 4, 4, 5, 1, 2, 6, 4, 2, 3, 5, 1, 2, 3, 4, 1, 2]],
]
expected = [
    [1, 20],
    [2, 19],
    [2, 21],
    [2, 19],
    [1, 19],
    [1, 21],
    [2, 19],
    [2, 12],
    [0, 0],
    [2, 19],
    [1, 18],
    [2, 20],
    [1, 21],
    [1, 19],
    [2, 21],
    [2, 16],
    [1, 17],
    [2, 20],
    [1, 16],
    [0, 0],
]

print("########### Testing Part II ###########")
for a, e in zip(args, expected):
    print('Testing blackjack_dice() with dice = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(blackjack_dice(*a)))
print('########################################')
print()



