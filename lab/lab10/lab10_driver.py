import sys
from package import *

student_file = 'lab10.py'

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

part_counts = [0] * 2
test_counts = [10, 10]

from lab10 import *

# Testing Part I
args = [
    [[Package("Monmouth", "Appleby", cost=0, distance=144), Package("Larkinge", "Ballachulish", cost=0, distance=791), Package("Malrton", "Auchtermuchty", cost=0, distance=872), Package("Monmouth", "Anghor Thom", cost=0, distance=937)], [10, 16, 37, 49]],
    [[Package("Satbury", "Burnsley", cost=0, distance=118), Package("Murrayfield", "Anghor Thom", cost=0, distance=736), Package("Appleby", "Aerilon", cost=0, distance=444)], [6, 31, 38, 44]],
    [[Package("Appleby", "Paentmarwy", cost=0, distance=396), Package("Jedborourgh", "Anghor Thom", cost=0, distance=160), Package("Appleby", "Aerilon", cost=0, distance=255), Package("Satbury", "Northpass", cost=0, distance=175), Package("Paentmarwy", "Bracklewhyte", cost=0, distance=844), Package("Auchtermuchty", "Anghor Thom", cost=0, distance=923)], [18, 32, 41, 48]],
    [[Package("Satbury", "Jedborourgh", cost=0, distance=811), Package("Bracklewhyte", "Ballachulish", cost=0, distance=785), Package("Erith", "Monmouth", cost=0, distance=469), Package("Aerilon", "Erith", cost=0, distance=866), Package("Anghor Thom", "Peltragow", cost=0, distance=629), Package("Larkinge", "Bracklewhyte", cost=0, distance=575), Package("Northpass", "Paentmarwy", cost=0, distance=925), Package("Monmouth", "Appleby", cost=0, distance=825), Package("Anghor Thom", "Appleby", cost=0, distance=349)], [12, 17, 38, 44]],
    [[Package("Bracklewhyte", "Monmouth", cost=0, distance=336), Package("Eanverness", "Monmouth", cost=0, distance=349), Package("Auchtermuchty", "Northpass", cost=0, distance=519)], [8, 13, 19, 36]],
    [[Package("Northpass", "Burnsley", cost=0, distance=491), Package("Paentmarwy", "Garennton", cost=0, distance=540), Package("Eanverness", "Monmouth", cost=0, distance=138), Package("Satbury", "Monmouth", cost=0, distance=474), Package("Paentmarwy", "Burnsley", cost=0, distance=736), Package("Satbury", "Erith", cost=0, distance=920), Package("Appleby", "Malrton", cost=0, distance=541), Package("Appleby", "Anghor Thom", cost=0, distance=141), Package("Ballachulish", "Burnsley", cost=0, distance=294), Package("Bracklewhyte", "Garennton", cost=0, distance=170)], [21, 28, 37, 48]],
    [[Package("Satbury", "Larkinge", cost=0, distance=954), Package("Satbury", "Jedborourgh", cost=0, distance=952), Package("Auchtermuchty", "Bracklewhyte", cost=0, distance=376), Package("Eanverness", "Bracklewhyte", cost=0, distance=271), Package("Malrton", "Ballachulish", cost=0, distance=735)], [8, 9, 18, 48]],
    [[Package("Northpass", "Erith", cost=0, distance=107)], [13, 28, 29, 44]],
    [[Package("Larkinge", "Bracklewhyte", cost=0, distance=839), Package("Burnsley", "Eanverness", cost=0, distance=153), Package("Monmouth", "Peltragow", cost=0, distance=123), Package("Monmouth", "Burnsley", cost=0, distance=882), Package("Auchtermuchty", "Murrayfield", cost=0, distance=349), Package("Peltragow", "Monmouth", cost=0, distance=676), Package("Paentmarwy", "Murrayfield", cost=0, distance=666), Package("Garennton", "Berkton", cost=0, distance=259)], [4, 10, 13, 41]],
    [[Package("Peltragow", "Paentmarwy", cost=0, distance=249), Package("Peltragow", "Monmouth", cost=0, distance=969), Package("Aerilon", "Monmouth", cost=0, distance=644), Package("Paentmarwy", "Berkton", cost=0, distance=222), Package("Auchtermuchty", "Paentmarwy", cost=0, distance=536), Package("Monmouth", "Larkinge", cost=0, distance=785), Package("Burnsley", "Paentmarwy", cost=0, distance=401)], [6, 10, 42, 43]],
]
expected_return_values = [
    163,
    113,
    233,
    384,
    74,
    378,
    171,
    28,
    207,
    234,
]
expected_updated_arguments = [
    [Package("Monmouth", "Appleby", cost=16, distance=144), Package("Larkinge", "Ballachulish", cost=49, distance=791), Package("Malrton", "Auchtermuchty", cost=49, distance=872), Package("Monmouth", "Anghor Thom", cost=49, distance=937)],
    [Package("Satbury", "Burnsley", cost=31, distance=118), Package("Murrayfield", "Anghor Thom", cost=44, distance=736), Package("Appleby", "Aerilon", cost=38, distance=444)],
    [Package("Appleby", "Paentmarwy", cost=41, distance=396), Package("Jedborourgh", "Anghor Thom", cost=32, distance=160), Package("Appleby", "Aerilon", cost=32, distance=255), Package("Satbury", "Northpass", cost=32, distance=175), Package("Paentmarwy", "Bracklewhyte", cost=48, distance=844), Package("Auchtermuchty", "Anghor Thom", cost=48, distance=923)],
    [Package("Satbury", "Jedborourgh", cost=44, distance=811), Package("Bracklewhyte", "Ballachulish", cost=44, distance=785), Package("Erith", "Monmouth", cost=38, distance=469), Package("Aerilon", "Erith", cost=44, distance=866), Package("Anghor Thom", "Peltragow", cost=44, distance=629), Package("Larkinge", "Bracklewhyte", cost=44, distance=575), Package("Northpass", "Paentmarwy", cost=44, distance=925), Package("Monmouth", "Appleby", cost=44, distance=825), Package("Anghor Thom", "Appleby", cost=38, distance=349)],
    [Package("Bracklewhyte", "Monmouth", cost=19, distance=336), Package("Eanverness", "Monmouth", cost=19, distance=349), Package("Auchtermuchty", "Northpass", cost=36, distance=519)],
    [Package("Northpass", "Burnsley", cost=37, distance=491), Package("Paentmarwy", "Garennton", cost=48, distance=540), Package("Eanverness", "Monmouth", cost=28, distance=138), Package("Satbury", "Monmouth", cost=37, distance=474), Package("Paentmarwy", "Burnsley", cost=48, distance=736), Package("Satbury", "Erith", cost=48, distance=920), Package("Appleby", "Malrton", cost=48, distance=541), Package("Appleby", "Anghor Thom", cost=28, distance=141), Package("Ballachulish", "Burnsley", cost=28, distance=294), Package("Bracklewhyte", "Garennton", cost=28, distance=170)],
    [Package("Satbury", "Larkinge", cost=48, distance=954), Package("Satbury", "Jedborourgh", cost=48, distance=952), Package("Auchtermuchty", "Bracklewhyte", cost=18, distance=376), Package("Eanverness", "Bracklewhyte", cost=9, distance=271), Package("Malrton", "Ballachulish", cost=48, distance=735)],
    [Package("Northpass", "Erith", cost=28, distance=107)],
    [Package("Larkinge", "Bracklewhyte", cost=41, distance=839), Package("Burnsley", "Eanverness", cost=10, distance=153), Package("Monmouth", "Peltragow", cost=10, distance=123), Package("Monmouth", "Burnsley", cost=41, distance=882), Package("Auchtermuchty", "Murrayfield", cost=13, distance=349), Package("Peltragow", "Monmouth", cost=41, distance=676), Package("Paentmarwy", "Murrayfield", cost=41, distance=666), Package("Garennton", "Berkton", cost=10, distance=259)],
    [Package("Peltragow", "Paentmarwy", cost=10, distance=249), Package("Peltragow", "Monmouth", cost=43, distance=969), Package("Aerilon", "Monmouth", cost=43, distance=644), Package("Paentmarwy", "Berkton", cost=10, distance=222), Package("Auchtermuchty", "Paentmarwy", cost=43, distance=536), Package("Monmouth", "Larkinge", cost=43, distance=785), Package("Burnsley", "Paentmarwy", cost=42, distance=401)],
]


print("############ Testing Part I ############")
for a, e, u in zip(args, expected_return_values, expected_updated_arguments):
    print('Testing shipping_cost() with packages =')
    for p in a[0]:
        print(f'   {p}')
    print(f'and cost_schedule = {a[1]}')
    print('Expected return value: {}'.format(e))
    actual = shipping_cost(*a)
    print('Actual return value:   {}'.format(actual))

    result = True
    print('Checking updated packages[] list...')
    if len(u) != len(a[0]):
        print('packages[] list has wrong length!')
        print('Expected:')
        for p in u:
            print(f'\t{p}')
        print('Actual:')
        for p in a[0]:
            print(f'\t{p}')

        result = False
    else:
        for p, q in zip(u, a[0]):
            result = result and p == q
            print(f'\tExpected: {p}')
            print(f'\tActual:   {q}')

    if e == actual and result:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
    print()
print('########################################')
print()


# Testing Part II
args = [
    [[('Burnsley', 'Ballachulish')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [5, 7, 16, 19]],
    [[('Appleby', 'Satbury'), ('Northpass', 'Berkton'), ('Eanverness', 'Satbury')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [18, 18, 24, 48]],
    [[('Murrayfield', 'Monmouth'), ('Bracklewhyte', 'Jedborourgh'), ('Bracklewhyte', 'Erith'), ('Eanverness', 'Jedborourgh'), ('Erith', 'Monmouth'), ('Paentmarwy', 'Northpass'), ('Paentmarwy', 'Anghor Thom'), ('Peltragow', 'Bracklewhyte'), ('Erith', 'Satbury'), ('Northpass', 'Paentmarwy')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [4, 9, 41, 49]],
    [[('Malrton', 'Burnsley')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [12, 15, 17, 37]],
    [[('Eanverness', 'Monmouth'), ('Garennton', 'Berkton'), ('Larkinge', 'Berkton'), ('Anghor Thom', 'Garennton')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [26, 28, 41, 44]],
    [[('Berkton', 'Erith'), ('Eanverness', 'Monmouth'), ('Appleby', 'Eanverness'), ('Eanverness', 'Paentmarwy'), ('Burnsley', 'Burnsley'), ('Eanverness', 'Burnsley')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [5, 22, 31, 48]],
    [[('Anghor Thom', 'Garennton')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [11, 16, 44, 46]],
    [[('Eanverness', 'Berkton'), ('Berkton', 'Monmouth'), ('Bracklewhyte', 'Malrton'), ('Satbury', 'Larkinge'), ('Jedborourgh', 'Appleby'), ('Berkton', 'Auchtermuchty'), ('Bracklewhyte', 'Malrton'), ('Northpass', 'Larkinge'), ('Malrton', 'Ballachulish')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [8, 9, 43, 48]],
    [[('Appleby', 'Aerilon'), ('Bracklewhyte', 'Northpass'), ('Aerilon', 'Paentmarwy'), ('Larkinge', 'Bracklewhyte')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [14, 31, 45, 50]],
    [[('Berkton', 'Malrton'), ('Aerilon', 'Monmouth'), ('Burnsley', 'Northpass'), ('Jedborourgh', 'Berkton'), ('Peltragow', 'Monmouth'), ('Larkinge', 'Monmouth')], {'Appleby': (58, 189), 'Berkton': (84, 13), 'Ballachulish': (12, 149), 'Aerilon': (28, 77), 'Garennton': (173, 68), 'Malrton': (124, 133), 'Peltragow': (194, 181), 'Paentmarwy': (191, 151), 'Eanverness': (134, 50), 'Satbury': (25, 181), 'Bracklewhyte': (47, 124), 'Larkinge': (8, 157), 'Burnsley': (71, 5), 'Erith': (2, 181), 'Monmouth': (160, 13), 'Northpass': (84, 45), 'Jedborourgh': (87, 163), 'Anghor Thom': (109, 10), 'Auchtermuchty': (140, 189), 'Murrayfield': (164, 83)}, [8, 17, 28, 39]],
]
expected_return_values = [
    [Package("Burnsley", "Ballachulish", cost=7, distance=155.6181223379848)],
    [Package("Appleby", "Satbury", cost=18, distance=33.95585369269929), Package("Northpass", "Berkton", cost=18, distance=32.0), Package("Eanverness", "Satbury", cost=18, distance=170.41713528867922)],
    [Package("Murrayfield", "Monmouth", cost=4, distance=70.11419257183242), Package("Bracklewhyte", "Jedborourgh", cost=4, distance=55.86591089385369), Package("Bracklewhyte", "Erith", cost=4, distance=72.62231062146122), Package("Eanverness", "Jedborourgh", cost=9, distance=122.38463955905577), Package("Erith", "Monmouth", cost=9, distance=230.62523712724936), Package("Paentmarwy", "Northpass", cost=9, distance=150.6154042586614), Package("Paentmarwy", "Anghor Thom", cost=9, distance=163.11039206623224), Package("Peltragow", "Bracklewhyte", cost=9, distance=157.66420012165096), Package("Erith", "Satbury", cost=4, distance=23.0), Package("Northpass", "Paentmarwy", cost=9, distance=150.6154042586614)],
    [Package("Malrton", "Burnsley", cost=15, distance=138.53880322855397)],
    [Package("Eanverness", "Monmouth", cost=26, distance=45.221676218380054), Package("Garennton", "Berkton", cost=28, distance=104.62313319720452), Package("Larkinge", "Berkton", cost=28, distance=162.82505949638096), Package("Anghor Thom", "Garennton", cost=26, distance=86.37129152675674)],
    [Package("Berkton", "Erith", cost=22, distance=186.9438418349211), Package("Eanverness", "Monmouth", cost=5, distance=45.221676218380054), Package("Appleby", "Eanverness", cost=22, distance=158.42032697857937), Package("Eanverness", "Paentmarwy", cost=22, distance=115.97413504743201), Package("Burnsley", "Burnsley", cost=5, distance=0.0), Package("Eanverness", "Burnsley", cost=5, distance=77.42092740338364)],
    [Package("Anghor Thom", "Garennton", cost=11, distance=86.37129152675674)],
    [Package("Eanverness", "Berkton", cost=8, distance=62.20128616033595), Package("Berkton", "Monmouth", cost=8, distance=76.0), Package("Bracklewhyte", "Malrton", cost=8, distance=77.52418977325722), Package("Satbury", "Larkinge", cost=8, distance=29.410882339705484), Package("Jedborourgh", "Appleby", cost=8, distance=38.948684188300895), Package("Berkton", "Auchtermuchty", cost=9, distance=184.69434208984313), Package("Bracklewhyte", "Malrton", cost=8, distance=77.52418977325722), Package("Northpass", "Larkinge", cost=9, distance=135.35139452550905), Package("Malrton", "Ballachulish", cost=9, distance=113.13708498984761)],
    [Package("Appleby", "Aerilon", cost=31, distance=115.94826432508596), Package("Bracklewhyte", "Northpass", cost=14, distance=87.23531395025755), Package("Aerilon", "Paentmarwy", cost=31, distance=179.0111728356641), Package("Larkinge", "Bracklewhyte", cost=14, distance=51.088159097779204)],
    [Package("Berkton", "Malrton", cost=17, distance=126.49110640673517), Package("Aerilon", "Monmouth", cost=17, distance=146.696966567138), Package("Burnsley", "Northpass", cost=8, distance=42.05948168962618), Package("Jedborourgh", "Berkton", cost=17, distance=150.02999700059985), Package("Peltragow", "Monmouth", cost=17, distance=171.40595088852663), Package("Larkinge", "Monmouth", cost=17, distance=209.3800372528384)],
]


print("############ Testing Part II ############")
for a, e in zip(args, expected_return_values):
    print('Testing package_tracking() with packages =')
    for p in a[0]:
        print(f'   {p}')
    print(f'and locations =')
    for k in a[1]:
        print(f'\t"{k}" -> {a[1][k]}')
    print(f'and cost_schedule = {a[2]}')
    actual = package_tracking(*a)

    result = True
    print('Checking updated packages[] list...')
    if actual is None:
        print('Function package_tracking() not implemented yet.')
        result = False
    elif len(e) != len(actual):
        print('Returned packages[] list has wrong length!')
        print('Expected:')
        for p in e:
            print(f'\t{p}')
        print('Actual:')
        for p in actual:
            print(f'\t{p}')

        result = False
    else:
        for p, q in zip(e, actual):
            result = result and p == q
            print(f'\tExpected: {p}')
            print(f'\tActual:   {q}')
    if result:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
    print()
print('########################################')
print()

print('Results:')
print(f'Part I:   {part_counts[0]}/{test_counts[0]}')
print(f'Part II:  {part_counts[1]}/{test_counts[1]}')
