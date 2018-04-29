from lab2 import *
import sys

student_file = 'lab2.py'

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

args = [
    [6.64, -5.02],
    [-9.15, 6.53],
    [9.66, 3.8],
    [-7.83, -9.59],
    [-9.01, 7.45],
    [-2.37, 1.62],
    [-0.9, 0.22],
    [9.08, 2.33],
    [5.56, -3.61],
    [6.83, -4.12],
]
expected = [
    0.9066265060240963,
    3.91,
    0.016019015218925313,
    -27.009999999999998,
    5.890000000000001,
    0.8700000000000001,
    -0.46,
    0.00725194157380947,
    0.829136690647482,
    0.7496339677891655,
]

for a, e in zip(args, expected):
    print('Testing compute2() with x = {}, y = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(compute2(*a)))

print()

args = [
    ['AMD', -0.1, 'hdd', 16.7],
    ['Intel', 0.0, 'SSD', 86.0],
    ['AMD', 3.5, 'HDD', 53.8],
    ['Intel', -0.1, 'HDD', 44.5],
    ['AMD', 1.4, 'HDD', 1.8],
    ['Intel', 2.8, 'SSD', 62.0],
    ['intel', 1.1, 'SSD', 82.5],
    ['AMD', 3.3, 'SSD', 63.9],
    ['AMD', 3.4, 'HDD', 48.8],
    ['Intel', 2.3, 'ssd', 97.9],
]
expected = [
    -1.0,
    -1.0,
    1532.6,
    -1.0,
    1358.6,
    1699.0,
    -1.0,
    1677.8,
    1522.6,
    -1.0,
]

for a, e in zip(args, expected):
    print('Testing computer_price() with cpu = {}, ghz = {}, disk_type = {}, disk_size = {}:'. \
          format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(computer_price(*a)))


