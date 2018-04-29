import sys

student_file = 'lab12.py'

f = open(student_file)
lines = f.readlines()
f.close()
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

part_counts = [0] * 3
test_counts = [10, 10, 10]

from lab12 import *

# Testing Part I
args = [
    [0b11100110001001101010010000],
    [0b1011110001000111110111100111],
    [0b101001110111110010110011000],
    [0b110010111111100001111100],
    [0b101100101001110100011010],
    [0b10010100111101],
    [0b11011000001],
    [0b1001100100000],
    [0b1000011111011],
    [0b1111011111100],
]
expected_return_values = [
    82,
    60,
    51,
    15,
    35,
    39,
    88,
    100,
    31,
    95,
]

print("############ Testing Part I ############")
for a, e in zip(args, expected_return_values):
    print(f'Testing extract_bits_3_9() with num = {bin(a[0])}')
    print('Expected: {}'.format(bin(e)))
    actual = extract_bits_3_9(*a)
    if actual is None:
        print('Actual:   None')
    else:
        print('Actual:   {}'.format(bin(actual)))
    if e == actual:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part II
args = [
    [0b111001100010100, [0, 9, 13, 5]],
    [0b11011000000101, [10, 4, 7]],
    [0b10000100101100100, [0, 3, 5, 6, 15, 16]],
    [0b10011100100110011, [0, 1]],
    [0b1010011110110011, [10, 13]],
    [0b1001011010010, [0, 10, 11, 5]],
    [0b1011100010011010, [9, 6]],
    [0b1111000100100, [3]],
    [0b101010110000000, [2]],
    [0b1110111001001111, [2, 7, 12, 14, 15]],
]
expected_return_values = [
    29493,
    13973,
    100717,
    80179,
    42931,
    7923,
    47834,
    7724,
    21892,
    65231,
]
for a, e in zip(args, expected_return_values):
    print(f'Testing bits_to_set() with num = {bin(a[0])}, bits_to_set = {a[1]}')
    print('Expected: {}'.format(bin(e)))
    actual = set_bits(*a)
    if actual is None:
        print('Actual:   None')
    else:
        print('Actual:   {}'.format(bin(actual)))
    if e == actual:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part III
args = [
    [0x01050000],
    [0x00040407],
    [0x01010207],
    [0x00090400],
    [0x00090005],
    [0x01050600],
    [0x04060614],
    [0x02000c05],
    [0x07020403],
    [0x04110752],
]
expected_return_values = [
    (1, 5, 0, 0),
    (0, 4, 4, 7),
    (1, 1, 2, 7),
    (0, 9, 4, 0),
    (0, 9, 0, 5),
    (1, 5, 6, 0),
    (4, 6, 1556),
    (-1, -1, -1, -1),
    (-1, -1, -1, -1),
    (-1, -1, -1, -1),
]

print("############ Testing Part III ############")
for a, e in zip(args, expected_return_values):
    to_hex = '0x' + ('0' * (10 - len(hex(a[0])))) + hex(a[0])[2:]
    print(f'Testing decode_instruction() with inst = {to_hex}')
    print('Expected: {}'.format(e))
    actual = decode_instruction(*a)
    print('Actual:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[2] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')
print(f'Part III: {part_counts[2]}/{test_counts[2]}')
