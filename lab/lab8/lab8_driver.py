import sys

student_file = 'lab8.py'

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

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()

part_counts = [0] * 2
test_counts = [10, 10]

from lab8 import *

# Testing Part I
args = [
    [{'Normal': 70, 'Double': 105, 'King': 195, 'Suite': 249}, 543, [['Normal', 1], ['Suite', 2], ['Double', 2], ['Normal', 1], ['King', 3]]],
    [{'Normal': 72, 'Double': 133, 'King': 192, 'Suite': 246}, 255, [['King', 3], ['Suite', 1], ['King', 1], ['Normal', 1], ['King', 2], ['Double', 3], ['Suite', 3]]],
    [{'Normal': 85, 'Double': 148, 'King': 190, 'Suite': 239}, 319, [['Suite', 1], ['Double', 1], ['Normal', 2], ['Double', 2], ['Double', 2], ['Suite', 2]]],
    [{'Normal': 99, 'Double': 104, 'King': 194, 'Suite': 275}, 516, [['Normal', 3], ['King', 2], ['Suite', 2], ['Normal', 3], ['Suite', 2], ['Double', 1]]],
    [{'Normal': 90, 'Double': 119, 'King': 158, 'Suite': 287}, 648, [['King', 2], ['Double', 1], ['Double', 3], ['King', 3], ['Double', 1]]],
    [{'Normal': 98, 'Double': 132, 'King': 169, 'Suite': 220}, 225, [['King', 1], ['King', 2], ['King', 2], ['King', 3], ['Double', 3], ['Double', 1]]],
    [{'Normal': 91, 'Double': 113, 'King': 181, 'Suite': 243}, 331, [['Suite', 3], ['Double', 3], ['Double', 2], ['Double', 3]]],
    [{'Normal': 76, 'Double': 124, 'King': 173, 'Suite': 291}, 0, [['Double', 1], ['King', 2], ['Double', 2]]],
    [{'Normal': 78, 'Double': 148, 'King': 183, 'Suite': 213}, 541, []],
    [{'Normal': 61, 'Double': 115, 'King': 196, 'Suite': 212}, 0, []],
]
expected_return_values = [
    (350, [['Normal', 1], ['Double', 2], ['Normal', 1]]),
    (246, [['Suite', 1]]),
    (239, [['Suite', 1]]),
    (401, [['Normal', 3], ['Double', 1]]),
    (554, [['King', 2], ['Double', 1], ['Double', 1]]),
    (169, [['King', 1]]),
    (226, [['Double', 2]]),
    (0, []),
    (0, []),
    (0, []),
]


print("############ Testing Part I ############")
for a, e in zip(args, expected_return_values):
    print('Testing vacation_calculator() with\n\troom_prices = {}\n\t'
          'budget = {}\n\treservations = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = vacation_calculator(*a)
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
    [{'Normal': 70, 'Double': 105, 'King': 195, 'Suite': 249}, {'Normal': 13, 'Double': 9, 'King': 5, 'Suite': 3}, [['Suite', 1], ['King', 3], ['Double', 6], ['King', 5], ['King', 3], ['King', 5]]],
    [{'Normal': 79, 'Double': 101, 'King': 190, 'Suite': 270}, {'Normal': 12, 'Double': 7, 'King': 7, 'Suite': 3}, [['King', 4], ['Double', 7], ['Suite', 2]]],
    [{'Normal': 60, 'Double': 128, 'King': 178, 'Suite': 226}, {'Normal': 11, 'Double': 8, 'King': 5, 'Suite': 4}, [['Suite', 1], ['King', 5], ['Suite', 2], ['Normal', 9]]],
    [{'Normal': 78, 'Double': 106, 'King': 193, 'Suite': 239}, {'Normal': 12, 'Double': 10, 'King': 6, 'Suite': 3}, [['Suite', 3], ['Double', 5], ['King', 3], ['Suite', 2], ['King', 4], ['Double', 5], ['Double', 7]]],
    [{'Normal': 97, 'Double': 144, 'King': 185, 'Suite': 242}, {'Normal': 11, 'Double': 7, 'King': 7, 'Suite': 4}, [['Normal', 10], ['King', 3], ['King', 4], ['King', 4]]],
    [{'Normal': 73, 'Double': 145, 'King': 160, 'Suite': 295}, {'Normal': 11, 'Double': 8, 'King': 7, 'Suite': 3}, [['King', 5], ['Double', 5], ['Suite', 1], ['Double', 6], ['Double', 7], ['Suite', 3]]],
    [{'Normal': 73, 'Double': 145, 'King': 162, 'Suite': 215}, {'Normal': 11, 'Double': 7, 'King': 6, 'Suite': 4}, [['Normal', 11], ['Normal', 11], ['Suite', 1], ['Suite', 1], ['Double', 7], ['Double', 5], ['Suite', 0]]],
    [{'Normal': 62, 'Double': 100, 'King': 164, 'Suite': 252}, {'Normal': 0, 'Double': 0, 'King': 0, 'Suite': 0}, []],
    [{'Normal': 60, 'Double': 124, 'King': 155, 'Suite': 296}, {'Normal': 12, 'Double': 8, 'King': 5, 'Suite': 4}, []],
    [{'Normal': 60, 'Double': 107, 'King': 155, 'Suite': 299}, {'Normal': 0, 'Double': 0, 'King': 0, 'Suite': 0}, []],
]
expected_return_values = [
    (1464, {'Suite': 249, 'King': 585, 'Double': 630}),
    (2007, {'King': 760, 'Double': 707, 'Suite': 540}),
    (2108, {'Suite': 678, 'King': 890, 'Normal': 540}),
    (2356, {'Suite': 717, 'Double': 1060, 'King': 579}),
    (2265, {'Normal': 970, 'King': 1295}),
    (1820, {'King': 800, 'Double': 725, 'Suite': 295}),
    (2248, {'Normal': 803, 'Suite': 430, 'Double': 1015}),
    (0, {}),
    (0, {}),
    (0, {}),
]

   

print("############ Testing Part II ############")
for a, e in zip(args, expected_return_values):
    print('Testing hotel_manager() with:\n\troom_prices = {}\n\troom_counts = {}\n\t'
          'reservations = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = hotel_manager(*a)
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
