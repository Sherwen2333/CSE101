from lab6 import *
import sys

student_file = 'lab6.py'

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

part_counts = [0] * 2
test_counts = [10, 10]

# Testing Part I
args = [
    [[['D'], ['A', 'A', 'C', 'D'], ['B'], ['C', 'F', 'C'], ['C', 'A', 'A', 'F', 'F', 'D'], ['D', 'D', 'C', 'F', 'B']]],
    [[['D'], ['D', 'B'], ['D', 'C', 'F', 'C', 'A', 'D']]],
    [[['F'], ['D', 'C', 'A', 'B'], ['C', 'F', 'C'], ['F', 'F'], ['C', 'B', 'B', 'A', 'F', 'F'], ['B', 'C', 'C', 'C'], ['F', 'C', 'B', 'B'], ['D', 'B', 'D', 'B', 'D', 'C']]],
    [[['D', 'F', 'C', 'B'], ['C', 'A', 'A', 'F', 'A'], ['A', 'F'], ['A', 'B'], ['A', 'A', 'F', 'A']]],
    [[['D', 'B', 'D', 'F'], ['D', 'B', 'D'], ['A', 'D'], ['D', 'B']]],
    [[['A'], ['B', 'C', 'A', 'D', 'B', 'A'], ['F', 'B', 'C', 'A', 'F', 'B'], ['A', 'B', 'F', 'A'], ['A', 'C', 'A'], ['C', 'B', 'B', 'F', 'F'], ['A', 'F'], ['D']]],
    [[['F', 'B'], ['B', 'B', 'D', 'F', 'D'], ['D'], ['D', 'B', 'C', 'D', 'A'], ['A', 'A', 'D', 'F', 'D', 'D'], ['A'], ['D', 'B'], ['C', 'F', 'A', 'B', 'A'], ['C', 'A', 'A', 'B', 'A']]],
    [[['A'], ['C', 'A'], ['C', 'B', 'C'], ['C'], ['F'], ['A'], ['B', 'B'], ['F', 'C', 'C', 'B', 'F', 'F'], ['B', 'A', 'F', 'D', 'D'], ['F']]],
    [[['A', 'A', 'B'], ['A', 'C', 'B', 'D', 'B', 'D'], ['A']]],
    [[['F', 'D', 'B']]],
]
expected = [
    ['R', 'G', 'G', 'R', 'Y', 'R'],
    ['R', 'Y', 'Y'],
    ['R', 'G', 'R', 'R', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'G', 'Y', 'G', 'G'],
    ['R', 'Y', 'G', 'Y'],
    ['G', 'G', 'Y', 'G', 'G', 'Y', 'Y', 'R'],
    ['Y', 'Y', 'R', 'Y', 'Y', 'G', 'Y', 'G', 'G'],
    ['G', 'G', 'Y', 'Y', 'R', 'G', 'G', 'R', 'Y', 'R'],
    ['G', 'Y', 'G'],
    ['R'],
]

print("############ Testing Part I ############")
for a, e in zip(args, expected):
    print('Testing student_alert() with orders = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = student_alert(*a)
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
    [[[('Level', 3), ('Salary', 30013), ('Experience', 2), ('Age', 25), ('Name', 'Charity')], [('Level', 3), ('Age', 23), ('Salary', 30003), ('Name', 'Leola'), ('Experience', 5)], [('Level', 5), ('Age', 19), ('Name', 'Melonie'), ('Experience', 1), ('Salary', 30001)], [('Experience', 4), ('Salary', 30005), ('Name', 'Ellan'), ('Level', 4), ('Age', 22)], [('Level', 2), ('Name', 'Elanor'), ('Age', 25), ('Experience', 4), ('Salary', 30007)], [('Level', 3), ('Name', 'Tiffany'), ('Age', 23), ('Experience', 1), ('Salary', 30014)]], 'Level', 2],
    [[[('Age', 21), ('Experience', 5), ('Level', 2), ('Salary', 30010), ('Name', 'Antony')], [('Name', 'Phebe'), ('Level', 3), ('Age', 25), ('Salary', 30010), ('Experience', 1)], [('Age', 20), ('Name', 'Eneida'), ('Level', 2), ('Salary', 30005), ('Experience', 2)], [('Name', 'Timmy'), ('Level', 2), ('Salary', 30015), ('Age', 20), ('Experience', 2)], [('Experience', 2), ('Salary', 30011), ('Level', 1), ('Name', 'Gertrud'), ('Age', 24)], [('Age', 20), ('Salary', 30010), ('Level', 5), ('Experience', 4), ('Name', 'Anderson')], [('Experience', 3), ('Salary', 30002), ('Name', 'Williams'), ('Level', 5), ('Age', 19)], [('Salary', 30000), ('Level', 2), ('Experience', 1), ('Name', 'Ellan'), ('Age', 20)], [('Level', 5), ('Age', 18), ('Experience', 1), ('Name', 'Aleshia'), ('Salary', 30003)], [('Name', 'Yuki'), ('Age', 25), ('Salary', 30007), ('Experience', 4), ('Level', 5)], [('Age', 23), ('Experience', 2), ('Level', 4), ('Salary', 30015), ('Name', 'Shantell')], [('Name', 'Tennille'), ('Level', 2), ('Salary', 30014), ('Age', 25), ('Experience', 2)], [('Level', 2), ('Salary', 30000), ('Name', 'Vickey'), ('Age', 18), ('Experience', 3)], [('Salary', 30011), ('Experience', 2), ('Level', 5), ('Age', 25), ('Name', 'Antone')]], 'Level', 1],
    [[[('Experience', 4), ('Age', 23), ('Level', 3), ('Salary', 30006), ('Name', 'Noble')], [('Experience', 3), ('Salary', 30006), ('Age', 21), ('Name', 'Ellan'), ('Level', 5)], [('Level', 1), ('Salary', 30001), ('Name', 'Isabelle'), ('Age', 20), ('Experience', 1)], [('Experience', 2), ('Salary', 30006), ('Level', 4), ('Name', 'Marianne'), ('Age', 24)], [('Level', 4), ('Salary', 30015), ('Experience', 5), ('Age', 19), ('Name', 'Zella')], [('Salary', 30000), ('Age', 20), ('Name', 'Melanie'), ('Experience', 2), ('Level', 1)], [('Salary', 30000), ('Age', 24), ('Experience', 5), ('Name', 'Molly'), ('Level', 2)], [('Level', 2), ('Name', 'Charlesetta'), ('Salary', 30000), ('Age', 19), ('Experience', 2)], [('Age', 23), ('Experience', 5), ('Salary', 30000), ('Level', 2), ('Name', 'Antony')], [('Salary', 30000), ('Age', 18), ('Level', 2), ('Experience', 3), ('Name', 'Elanor')], [('Level', 3), ('Experience', 2), ('Age', 19), ('Salary', 30000), ('Name', 'Leola')]], 'Salary', 30006],
    [[[('Name', 'Ivonne'), ('Experience', 3), ('Salary', 30009), ('Age', 23), ('Level', 5)], [('Experience', 1), ('Salary', 30010), ('Age', 25), ('Name', 'Lyn'), ('Level', 5)], [('Age', 21), ('Level', 2), ('Salary', 30013), ('Name', 'Eneida'), ('Experience', 3)], [('Age', 23), ('Level', 1), ('Salary', 30005), ('Experience', 1), ('Name', 'Katheleen')], [('Salary', 30000), ('Experience', 4), ('Name', 'Dominick'), ('Level', 3), ('Age', 25)], [('Experience', 1), ('Age', 19), ('Level', 1), ('Salary', 30010), ('Name', 'Jose')], [('Level', 4), ('Experience', 2), ('Age', 20), ('Name', 'Wilton'), ('Salary', 30000)], [('Experience', 2), ('Name', 'Isabelle'), ('Level', 3), ('Age', 22), ('Salary', 30004)], [('Name', 'Janita'), ('Experience', 4), ('Level', 5), ('Salary', 30007), ('Age', 18)]], 'Experience', 2],
    [[[('Level', 1), ('Age', 25), ('Salary', 30008), ('Experience', 5), ('Name', 'Janice')], [('Name', 'Jose'), ('Level', 1), ('Salary', 30011), ('Experience', 5), ('Age', 23)], [('Experience', 1), ('Age', 22), ('Name', 'Chance'), ('Level', 2), ('Salary', 30015)], [('Name', 'Erminia'), ('Salary', 30006), ('Experience', 4), ('Level', 5), ('Age', 18)], [('Salary', 30014), ('Level', 4), ('Experience', 2), ('Name', 'Wilton'), ('Age', 19)], [('Name', 'Bibi'), ('Age', 19), ('Salary', 30008), ('Experience', 2), ('Level', 2)], [('Salary', 30000), ('Age', 23), ('Level', 4), ('Name', 'Henry'), ('Experience', 3)], [('Age', 18), ('Salary', 30009), ('Experience', 3), ('Level', 1), ('Name', 'Tyesha')], [('Name', 'Bethany'), ('Age', 21), ('Salary', 30002), ('Experience', 5), ('Level', 5)], [('Salary', 30013), ('Experience', 3), ('Name', 'Sofia'), ('Age', 20), ('Level', 3)], [('Name', 'Tiffany'), ('Level', 3), ('Salary', 30007), ('Experience', 3), ('Age', 23)], [('Level', 2), ('Age', 20), ('Name', 'Darryl'), ('Experience', 3), ('Salary', 30008)], [('Level', 1), ('Experience', 5), ('Name', 'Twila'), ('Age', 23), ('Salary', 30014)], [('Salary', 30014), ('Name', 'Aleshia'), ('Experience', 1), ('Age', 23), ('Level', 2)], [('Experience', 1), ('Name', 'Armandina'), ('Level', 4), ('Age', 21), ('Salary', 30010)]], 'Experience', 1],
    [[[('Experience', 1), ('Salary', 30009), ('Age', 23), ('Name', 'Zella'), ('Level', 1)], [('Age', 25), ('Name', 'Williams'), ('Level', 5), ('Salary', 30014), ('Experience', 4)], [('Salary', 30012), ('Level', 4), ('Age', 24), ('Name', 'Molly'), ('Experience', 4)], [('Name', 'Richelle'), ('Experience', 1), ('Level', 3), ('Salary', 30012), ('Age', 20)]], 'Salary', 30000],
    [[[('Age', 19), ('Name', 'Eneida'), ('Salary', 30003), ('Level', 4), ('Experience', 4)], [('Age', 25), ('Salary', 30003), ('Experience', 2), ('Name', 'Noel'), ('Level', 1)], [('Salary', 30010), ('Level', 4), ('Experience', 2), ('Name', 'Wilton'), ('Age', 24)], [('Level', 3), ('Salary', 30000), ('Age', 25), ('Name', 'Lourdes'), ('Experience', 3)], [('Salary', 30002), ('Age', 25), ('Experience', 3), ('Name', 'Tyesha'), ('Level', 4)], [('Level', 3), ('Experience', 5), ('Age', 22), ('Name', 'Shantell'), ('Salary', 30015)], [('Level', 3), ('Salary', 30015), ('Experience', 5), ('Name', 'Jeanine'), ('Age', 24)], [('Name', 'Janita'), ('Salary', 30015), ('Level', 5), ('Age', 21), ('Experience', 1)], [('Level', 4), ('Age', 23), ('Name', 'Adrianna'), ('Salary', 30014), ('Experience', 5)], [('Age', 20), ('Salary', 30006), ('Experience', 5), ('Name', 'Darryl'), ('Level', 3)], [('Age', 21), ('Name', 'Walton'), ('Level', 3), ('Experience', 3), ('Salary', 30002)], [('Level', 1), ('Salary', 30009), ('Name', 'Leola'), ('Age', 20), ('Experience', 1)], [('Experience', 2), ('Level', 3), ('Name', 'Mirta'), ('Salary', 30003), ('Age', 25)], [('Salary', 30007), ('Name', 'Zella'), ('Level', 3), ('Age', 18), ('Experience', 2)], [('Level', 1), ('Salary', 30005), ('Name', 'Terese'), ('Experience', 1), ('Age', 20)]], 'Salary', 30015],
    [[[('Name', 'Jacinda'), ('Experience', 5), ('Age', 20), ('Salary', 30012), ('Level', 2)], [('Salary', 30009), ('Level', 1), ('Age', 18), ('Experience', 2), ('Name', 'Vernita')], [('Name', 'Chance'), ('Age', 24), ('Level', 5), ('Salary', 30012), ('Experience', 3)], [('Name', 'Erminia'), ('Salary', 30003), ('Experience', 3), ('Age', 23), ('Level', 4)], [('Age', 22), ('Name', 'Yuko'), ('Experience', 3), ('Level', 1), ('Salary', 30004)], [('Name', 'Emily'), ('Level', 5), ('Experience', 4), ('Age', 23), ('Salary', 30005)], [('Level', 4), ('Salary', 30007), ('Age', 21), ('Experience', 2), ('Name', 'Dominick')], [('Level', 1), ('Experience', 1), ('Age', 21), ('Salary', 30001), ('Name', 'Lorriane')], [('Salary', 30015), ('Level', 4), ('Name', 'Bethany'), ('Experience', 3), ('Age', 18)], [('Age', 24), ('Name', 'Mozell'), ('Salary', 30008), ('Level', 2), ('Experience', 5)], [('Age', 22), ('Name', 'Delisa'), ('Experience', 3), ('Salary', 30013), ('Level', 3)]], 'Level', 5],
    [[[('Salary', 30012), ('Age', 20), ('Level', 1), ('Name', 'Parthenia'), ('Experience', 4)], [('Age', 19), ('Salary', 30012), ('Name', 'Mirta'), ('Experience', 2), ('Level', 4)], [('Experience', 2), ('Name', 'Genevieve'), ('Level', 3), ('Salary', 30011), ('Age', 19)], [('Experience', 3), ('Age', 20), ('Salary', 30008), ('Level', 1), ('Name', 'Shemeka')], [('Experience', 1), ('Name', 'Dominick'), ('Age', 20), ('Level', 4), ('Salary', 30009)], [('Age', 21), ('Level', 3), ('Salary', 30012), ('Experience', 3), ('Name', 'Melanie')], [('Age', 19), ('Level', 2), ('Name', 'Armandina'), ('Experience', 4), ('Salary', 30010)], [('Level', 4), ('Name', 'Wallace'), ('Experience', 5), ('Salary', 30000), ('Age', 24)], [('Experience', 2), ('Name', 'Randi'), ('Level', 2), ('Salary', 30014), ('Age', 22)], [('Name', 'Williams'), ('Salary', 30010), ('Experience', 2), ('Age', 20), ('Level', 5)], [('Age', 25), ('Experience', 5), ('Salary', 30006), ('Name', 'Sofia'), ('Level', 5)], [('Salary', 30007), ('Level', 3), ('Experience', 3), ('Age', 18), ('Name', 'Glennis')]], 'Age', 25],
    [[[('Experience', 1), ('Age', 19), ('Level', 4), ('Salary', 30010), ('Name', 'Regena')], [('Salary', 30007), ('Age', 20), ('Name', 'Jerold'), ('Experience', 5), ('Level', 4)]], 'Age', 20],
]
expected = [
    ['Elanor'],
    ['Gertrud'],
    ['Noble', 'Ellan', 'Marianne'],
    ['Wilton', 'Isabelle'],
    ['Chance', 'Aleshia', 'Armandina'],
    [],
    ['Shantell', 'Jeanine', 'Janita'],
    ['Chance', 'Emily'],
    ['Sofia'],
    ['Jerold'],
]

print("############ Testing Part II ############")
for a, e in zip(args, expected):
    print('Testing find_employee() with orders = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = find_employee(*a)
    print('Actual:   {}'.format(actual))
    if actual is not None and sorted(e) == sorted(actual):
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')