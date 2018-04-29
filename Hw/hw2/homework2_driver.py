from homework2 import *

import sys

student_file = 'homework2.py'

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

# Part I Testing
args = [
    [-9, 1],
    [5, 9],
    [-5, -3],
    [-7, -2],
    [6, 9],
    [0, 10],
    [-4, 8],
    [2, 3],
    [-6, 9],
    [-9, 4],
]
expected = [
    -2145.0,
    1961.6666666666665,
    -249.0,
    -854.0,
    1832.6666666666665,
    3069.0,
    1183.0,
    34.66666666666667,
    1554.6666666666665,
    -2044.0000000000002,
]

print("########## Testing Part I ##########")
for a, e in zip(args, expected):
    print('Testing summation() with x = {}, y = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(summation(*a)))
print('########################################')
print()

# Part II Testing
args = [
    [1995, 'Regular', 74.95480578251386],
    [870, 'Regular', -23.705557429821557],
    [3054, 'Good', 27.80750330446164],
    [4933, 'Plus', 76.85532456142764],
    [393, 'Regular', -7.245453064858392],
    [1981, 'Plus', 5.838288853611488],
    [4989, 'Regular', -29.623101627776485],
    [3033, 'Premium', 54.08601795248893],
    [1792, 'Plus', 25.587222964208976],
    [4666, 'Regular', 57.73657576959238],
    [-5, 'Plus', 58.933838226988605],
]
expected = [
    2545,
    870,
    'unavailable',
    5483,
    393,
    2006,
    4989,
    3433,
    1917,
    5216,
    'error',
]

print("########## Testing Part II ##########")
for a, e in zip(args, expected):
    print('Testing gas_reward() with current_points = {}, gas_type = {}, money_spent = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(gas_reward(*a)))
print('########################################')
print()

# Part III Testing
args = [
    [['Z9', 'gbd2xKC', '7MWt0', 'dcl2'], 1],
    [['GMca', 'xuP5S'], 1],
    [['p8K5m', 'OvnLHqz'], 6],
    [['QGqj3ZM', 'ZD', 'fU2eN81n', 'RztBk', 'ySTuI1', 'FHLoDVw0', 'WUybIBOA'], 1],
    [['vFmq', '5wVxmCT'], 6],
    [['EXdfk', 'T2RCPQn5'], 0],
    [['Q7A', '4Dhm8G1j', 'BQ1FH'], 0],
    [['YFnOfD', 'o2eMrAY', 'EofzJ', 'OxEot13z', 'jmksbi'], 5],
    [['yCZMkI', '2i'], 2],
    [['iL', 'C8n7', 'vj5gq', 'n1', 'NJ20EYMx', 'D9ylhBQ', 'mr15iUX', 'zS'], 4],
]
expected = [
    ['9', 'b', 'M', 'c'],
    ['M', 'u'],
    ['z'],
    ['G', 'D', 'U', 'z', 'S', 'H', 'U'],
    ['T'],
    ['E', 'T'],
    ['Q', '4', 'B'],
    ['D', 'A', '1', 'i'],
    ['Z'],
    ['q', 'E', 'h', 'i'],
]

print("########## Testing Part III ##########")
for a, e in zip(args, expected):
    print('Testing pull() with strings = {}, i = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(pull(*a)))
print('########################################')
print()

# Part IV Testing
args = [
    [['Legal', 'Gray Scale', 44]],
    [['Letter', 'Gray Scale', 4]],
    [['A4', 'Colored', 32]],
    [['A4', 'Colored', 4]],
    [['Letter', 'Gray Scale', 16]],
    [['Letter', 'Colored', 33]],
    [['Letter', 'Gray Scale', 32]],
    [['A4', 'Colored', 42]],
    [['Legal', 'Gray Scale', 28]],
    [['Legal', 'Gray Scale', 44]],
]
expected = [
    3.0799999999999996,
    0.24000000000000002,
    4.96,
    0.62,
    0.9600000000000001,
    4.950000000000001,
    1.9200000000000002,
    6.51,
    1.9599999999999997,
    3.0799999999999996,
]

print("########## Testing Part IV ##########")
for a, e in zip(args, expected):
    print('Testing print_cost() with task = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(print_cost(*a)))
print('########################################')
print()

# Part V Testing
args = [
    [6, [[6, 'A5', 'Gray Scale', 25], [2, 'Legal', 'Colored', 33], [7, 'A4', 'Colored', 15], [2, 'A5', 'Colored', 39],
         [4, 'A4', 'Gray Scale', 47], [5, 'A4', 'Colored', 13], [8, 'Letter', 'Gray Scale', 33],
         [6, 'Legal', 'Gray Scale', 17], [8, 'Letter', 'Colored', 39]]],
    [3, [[8, 'Legal', 'Gray Scale', 30], [3, 'A5', 'Colored', 43], [8, 'Letter', 'Colored', 31]]],
    [6, [[2, 'Legal', 'Colored', 33], [6, 'A4', 'Gray Scale', 5], [6, 'Legal', 'Colored', 26]]],
    [8, [[8, 'Legal', 'Colored', 48]]],
    [8, [[8, 'Letter', 'Gray Scale', 33], [1, 'Legal', 'Colored', 39], [4, 'A4', 'Gray Scale', 47],
         [8, 'A5', 'Colored', 36], [8, 'Letter', 'Colored', 39], [8, 'Letter', 'Gray Scale', 38],
         [4, 'A5', 'Gray Scale', 35], [5, 'A5', 'Gray Scale', 13], [8, 'Letter', 'Colored', 31]]],
    [8, [[8, 'Letter', 'Gray Scale', 38], [8, 'Legal', 'Gray Scale', 30], [8, 'Legal', 'Gray Scale', 33],
         [8, 'A5', 'Colored', 36], [8, 'Legal', 'Colored', 48], [7, 'A5', 'Gray Scale', 6]]],
    [8, [[8, 'Letter', 'Colored', 31], [8, 'Legal', 'Gray Scale', 33], [6, 'A4', 'Gray Scale', 5],
         [4, 'A4', 'Gray Scale', 47], [2, 'A5', 'Colored', 39], [8, 'Letter', 'Colored', 39],
         [7, 'A4', 'Gray Scale', 39], [7, 'Legal', 'Colored', 3], [7, 'A5', 'Gray Scale', 8]]],
    [3, [[10, 'A4', 'Colored', 4], [9, 'A4', 'Colored', 30], [4, 'A5', 'Colored', 41], [3, 'A5', 'Colored', 43],
         [1, 'A5', 'Gray Scale', 47], [8, 'Legal', 'Colored', 48], [1, 'Letter', 'Gray Scale', 3],
         [6, 'A5', 'Gray Scale', 35], [8, 'Letter', 'Gray Scale', 38], [6, 'A4', 'Colored', 13]]],
    [8, [[6, 'A5', 'Gray Scale', 35], [8, 'Legal', 'Colored', 39], [7, 'A4', 'Colored', 44], [10, 'A4', 'Colored', 4],
         [1, 'Letter', 'Gray Scale', 3], [7, 'A5', 'Gray Scale', 8], [1, 'Legal', 'Colored', 39],
         [7, 'Legal', 'Colored', 3], [3, 'A5', 'Colored', 43], [4, 'Letter', 'Colored', 27]]],
    [9, [[9, 'A4', 'Colored', 30]]],
]
expected = [
    2.44,
    6.0200000000000005,
    4.485,
    7.68,
    19.800000000000004,
    19.41,
    12.81,
    6.0200000000000005,
    6.24,
    4.65,
]

print("########## Testing Part V ##########")
for a, e in zip(args, expected):
    print('Testing total_cost() with ID = {}, tasks = {}:'.format(*a))
    print('Expected: {}'.format(e))
    print('Actual:   {}'.format(total_cost(*a)))
print('########################################')

