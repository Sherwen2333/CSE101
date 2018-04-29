import sys

def check_dictionary(expected, actual):
    if len(expected) != len(actual):
        return False

    for key in expected:
        if key in actual:
            if not isinstance(actual[key], type(expected[key])):
                return False
            if actual[key] != expected[key]:
                return False
        else:
            return False
    return True

student_file = 'homework4.py'

lines = open(student_file).readlines()
lines = [line.strip() for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'input' in lines[i] and not lines[i].startswith('#'):
        print('Line {} of {} contains an input() statement. You must delete this line.'. \
              format(i, student_file))
        code_clean = False
    if 'exit' in lines[i] or 'sys.exit' in lines[i]:
        print('Line {} of {} contains an exit() statement. You must delete this line.'. \
              format(i, student_file))

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()

from homework4 import *

part_counts = [0] * 5
test_counts = [20, 10, 10, 15, 20]

# Testing Part I
args = [
    ['f^BAcG'],
    ['tlX'],
    ['W63UtHTuN'],
    ['f'],
    ['Msq08#2w&GpMm'],
    ['qHjTt9YQ'],
    ['gw74X5I2'],
    ['&9@%B9T(jZJ'],
    ['y*n(q%XxVp2'],
    ['!fxus'],
    ['@l1V*l'],
    ['pJSmXIqrmUD'],
    ['Annulx%'],
    ['!$p$egYSW'],
    ['(Q*Zjbg6aDh2'],
    ['x*rX4HP#xI'],
    ['%gU'],
    ['gFVI'],
    ['1dawHi488zrQ'],
    ['R'],
]
expected_return_values = [
    360,
    75,
    1170,
    5,
    2275,
    680,
    1240,
    1870,
    1540,
    225,
    510,
    990,
    595,
    945,
    2040,
    1150,
    135,
    160,
    2040,
    40,
]

print("############ Testing Part I ############")
for a, e in zip(args, expected_return_values):
    print('Testing password_strength() with password = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = password_strength(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[0] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part II
args = [
    [{'soda': 8, 'burger': 5, 'chips': 5, 'pizza': 7}, ['pizza', 'pizza', 'burger', 'pizza', 'pizza', 'burger', 'burger']],
    [{'burger': 4, 'chips': 10, 'pizza': 6, 'soda': 3}, ['soda', 'salad', 'pizza', 'soda', 'chips', 'burger', 'sandwich']],
    [{'soda': 4, 'chips': 4, 'pizza': 8, 'burger': 9}, ['soda', 'chips', 'chips', 'burger', 'pizza', 'chips', 'soda', 'soup']],
    [{'chips': 4, 'soda': 6, 'pizza': 6, 'burger': 4}, ['burger', 'pizza', 'burger', 'soup', 'burger', 'soda', 'soda']],
    [{'soda': 3, 'pizza': 5, 'burger': 6, 'chips': 6}, ['steak', 'chips', 'soda', 'chips', 'burger', 'soda', 'chips', 'chips', 'pizza']],
    [{'burger': 5, 'soda': 2, 'pizza': 3, 'chips': 1}, ['pizza', 'soda', 'pizza', 'burger', 'burger', 'chips', 'pizza', 'chips', 'soda', 'chips', 'chips', 'burger', 'burger', 'soda']],
    [{'burger': 3, 'pizza': 4, 'chips': 3, 'soda': 0}, ['steak', 'soda', 'soup', 'chips', 'soda', 'steak', 'soda', 'soda', 'chips', 'soda', 'pizza', 'burger', 'pizza', 'chips', 'chips', 'soda', 'chips']],
    [{'burger': 4, 'chips': 3, 'pizza': 3, 'soda': 2}, ['salad', 'soda', 'pizza', 'soda', 'burger', 'soda', 'chips', 'soda', 'steak', 'burger', 'soda', 'burger', 'burger', 'burger', 'burger', 'soup']],
    [{'chips': 5, 'soda': 3, 'burger': 3, 'pizza': 1}, ['soda', 'chips', 'pizza', 'pizza', 'chips', 'salad', 'chips', 'steak', 'soda', 'soda', 'chips', 'burger', 'pizza']],
    [{'soda': 4, 'chips': 4, 'burger': 6, 'pizza': 0}, ['chips', 'chips', 'burger', 'burger', 'soda', 'pizza', 'pizza', 'chips', 'soda', 'burger', 'pizza', 'soda', 'soda', 'soup', 'burger', 'pizza', 'soup', 'steak']],
]
expected_return_values = [
    7,
    5,
    7,
    6,
    8,
    10,
    6,
    8,
    9,
    11,
]
updated_arguments = [
    {'soda': 8, 'burger': 2, 'chips': 5, 'pizza': 3},
    {'burger': 3, 'chips': 9, 'pizza': 5, 'soda': 1},
    {'soda': 2, 'chips': 1, 'pizza': 7, 'burger': 8},
    {'chips': 4, 'soda': 4, 'pizza': 5, 'burger': 1},
    {'soda': 1, 'pizza': 4, 'burger': 5, 'chips': 2},
    {'burger': 1, 'soda': 0, 'pizza': 0, 'chips': 0},
    {'burger': 2, 'pizza': 2, 'chips': 0, 'soda': 0},
    {'burger': 0, 'chips': 2, 'pizza': 2, 'soda': 0},
    {'chips': 1, 'soda': 0, 'burger': 2, 'pizza': 0},
    {'soda': 0, 'chips': 1, 'burger': 2, 'pizza': 0},
]

print("############ Testing Part II ############")
for a, e, u in zip(args, expected_return_values, updated_arguments):
    print('Testing order_lunches() with stock = {}, orders = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = order_lunches(*a)
    stock_ok = check_dictionary(u, a[0])
    print('Actual Return Value:   {}'.format(actual))
    print(f'Expected Updated stock: {u}')
    print(f'Actual Updated stock:   {a[0]}')
    if e == actual and stock_ok:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()

# Testing Part III
args = [
    ['Africa', 1529760, {'Americas': ['Argentina', 'Uruguay', 'Brazil', 'Puerto Rico', 'Panama'], 'Oceania': ['Fiji', 'Australia', 'New Zealand', 'Papua New Guinea'], 'Asia': ['Myanmar', 'Israel'], 'Africa': ['Senegal', 'Lesotho', 'South Africa', 'Togo', 'Sierra Leone'], 'Europe': ['Norway', 'Greece']}, {'Argentina': 545866, 'Uruguay': 52420, 'Brazil': 1796186, 'Puerto Rico': 103135, 'Panama': 55188, 'Fiji': 4632, 'Australia': 1204616, 'New Zealand': 185017, 'Papua New Guinea': 16929, 'Myanmar': 67430, 'Israel': 318744, 'Senegal': 14765, 'Lesotho': 2200, 'South Africa': 294841, 'Togo': 4400, 'Sierra Leone': 3669, 'Norway': 370557, 'Greece': 194559}, {'Argentina': 43847430, 'Uruguay': 3444006, 'Brazil': 207652865, 'Puerto Rico': 3667903, 'Panama': 4034119, 'Fiji': 898760, 'Australia': 24125848, 'New Zealand': 4660833, 'Papua New Guinea': 8084991, 'Myanmar': 52885223, 'Israel': 8191828, 'Senegal': 15411614, 'Lesotho': 2203821, 'South Africa': 56015473, 'Togo': 7606374, 'Sierra Leone': 7396190, 'Norway': 5254694, 'Greece': 11183716}],
    ['Africa', 42690, {'Americas': ['Panama', 'Guatemala'], 'Oceania': ['New Zealand', 'Australia', 'Fiji'], 'Asia': ['Vietnam', 'South Korea', 'Israel'], 'Africa': ['Lesotho', 'Burundi', 'Algeria', 'Cameroon', 'Angola'], 'Europe': ['Finland', 'Luxembourg', 'Russia', 'Belarus', 'Ukraine']}, {'Panama': 55188, 'Guatemala': 68763, 'New Zealand': 185017, 'Australia': 1204616, 'Fiji': 4632, 'Vietnam': 202616, 'South Korea': 1411246, 'Israel': 318744, 'Lesotho': 2200, 'Burundi': 3007, 'Algeria': 156080, 'Cameroon': 24204, 'Angola': 89633, 'Finland': 236785, 'Luxembourg': 59948, 'Russia': 1283162, 'Belarus': 47433, 'Ukraine': 93270}, {'Panama': 4034119, 'Guatemala': 16582469, 'New Zealand': 4660833, 'Australia': 24125848, 'Fiji': 898760, 'Vietnam': 94569072, 'South Korea': 50791919, 'Israel': 8191828, 'Lesotho': 2203821, 'Burundi': 10524117, 'Algeria': 40606052, 'Cameroon': 23439189, 'Angola': 28813463, 'Finland': 5503132, 'Luxembourg': 575747, 'Russia': 143964513, 'Belarus': 9480042, 'Ukraine': 44438625}],
    ['Oceania', 386428, {'Americas': ['Peru', 'Dominican Republic', 'United States'], 'Oceania': ['New Zealand', 'Australia'], 'Asia': ['India', 'Jordan', 'Tajikistan'], 'Africa': ['Benin', 'Central African Republic', 'South Africa', 'Namibia', 'Rwanda'], 'Europe': ['Germany', 'Luxembourg', 'Russia']}, {'Peru': 192094, 'Dominican Republic': 71584, 'United States': 18624475, 'New Zealand': 185017, 'Australia': 1204616, 'India': 2263792, 'Jordan': 38655, 'Tajikistan': 6952, 'Benin': 8583, 'Central African Republic': 1756, 'South Africa': 294841, 'Namibia': 10267, 'Rwanda': 8376, 'Germany': 3477796, 'Luxembourg': 59948, 'Russia': 1283162}, {'Peru': 31773839, 'Dominican Republic': 10648791, 'United States': 322179605, 'New Zealand': 4660833, 'Australia': 24125848, 'India': 1324171354, 'Jordan': 9455802, 'Tajikistan': 8734951, 'Benin': 10872298, 'Central African Republic': 4594621, 'South Africa': 56015473, 'Namibia': 2479713, 'Rwanda': 11917508, 'Germany': 81914672, 'Luxembourg': 575747, 'Russia': 143964513}],
    ['Americas', 3446, {'Americas': ['Venezuela', 'Barbados', 'Panama', 'Ecuador', 'Bermuda'], 'Oceania': ['Papua New Guinea', 'Australia', 'Fiji', 'New Zealand'], 'Asia': ['Qatar', 'Macau', 'Singapore', 'Thailand'], 'Africa': ['Zambia', 'Madagascar', 'Equatorial Guinea', 'Niger', 'Libya'], 'Europe': ['Russia', 'Netherlands', 'Czech Republic', 'France']}, {'Venezuela': 371337, 'Barbados': 4588, 'Panama': 55188, 'Ecuador': 97802, 'Bermuda': 5574, 'Papua New Guinea': 16929, 'Australia': 1204616, 'Fiji': 4632, 'New Zealand': 185017, 'Qatar': 152469, 'Macau': 44803, 'Singapore': 296966, 'Thailand': 406840, 'Zambia': 19551, 'Madagascar': 9991, 'Equatorial Guinea': 10179, 'Niger': 7509, 'Libya': 29153, 'Russia': 1283162, 'Netherlands': 777227, 'Czech Republic': 192925, 'France': 2465453}, {'Venezuela': 31568179, 'Barbados': 284996, 'Panama': 4034119, 'Ecuador': 16385068, 'Bermuda': 61666, 'Papua New Guinea': 8084991, 'Australia': 24125848, 'Fiji': 898760, 'New Zealand': 4660833, 'Qatar': 2569804, 'Macau': 612167, 'Singapore': 5622455, 'Thailand': 68863514, 'Zambia': 16591390, 'Madagascar': 24894551, 'Equatorial Guinea': 1221490, 'Niger': 20672987, 'Libya': 6293253, 'Russia': 143964513, 'Netherlands': 16987330, 'Czech Republic': 10610947, 'France': 64720690}],
    ['Africa', 4632, {'Americas': ['Venezuela', 'Brazil'], 'Oceania': ['Papua New Guinea', 'New Zealand', 'Fiji', 'Australia'], 'Asia': ['Azerbaijan', 'Vietnam', 'Kuwait', 'Japan', 'Qatar'], 'Africa': ['Cameroon', 'Cape Verde'], 'Europe': ['Finland', 'Moldova', 'Malta', 'Croatia']}, {'Venezuela': 371337, 'Brazil': 1796186, 'Papua New Guinea': 16929, 'New Zealand': 185017, 'Fiji': 4632, 'Australia': 1204616, 'Azerbaijan': 37848, 'Vietnam': 202616, 'Kuwait': 112812, 'Japan': 4940158, 'Qatar': 152469, 'Cameroon': 24204, 'Cape Verde': 1617, 'Finland': 236785, 'Moldova': 6750, 'Malta': 10949, 'Croatia': 50425}, {'Venezuela': 31568179, 'Brazil': 207652865, 'Papua New Guinea': 8084991, 'New Zealand': 4660833, 'Fiji': 898760, 'Australia': 24125848, 'Azerbaijan': 9725376, 'Vietnam': 94569072, 'Kuwait': 4052584, 'Japan': 127748513, 'Qatar': 2569804, 'Cameroon': 23439189, 'Cape Verde': 539560, 'Finland': 5503132, 'Moldova': 4059608, 'Malta': 429362, 'Croatia': 4213265}],
    ['Asia', 89633, {'Americas': ['El Salvador', 'Dominican Republic', 'Guatemala', 'Honduras', 'Panama'], 'Oceania': ['Papua New Guinea', 'Australia'], 'Asia': ['Israel', 'Cyprus', 'Philippines', 'Brunei', 'Saudi Arabia'], 'Africa': ['Kenya', 'Cameroon', 'Ghana', 'Tunisia', 'Rwanda'], 'Europe': ['Austria', 'Portugal', 'Belarus', 'Iceland', 'Slovakia']}, {'El Salvador': 26797, 'Dominican Republic': 71584, 'Guatemala': 68763, 'Honduras': 21517, 'Panama': 55188, 'Papua New Guinea': 16929, 'Australia': 1204616, 'Israel': 318744, 'Cyprus': 19802, 'Philippines': 304905, 'Brunei': 11400, 'Saudi Arabia': 646438, 'Kenya': 70529, 'Cameroon': 24204, 'Ghana': 42690, 'Tunisia': 42063, 'Rwanda': 8376, 'Austria': 386428, 'Portugal': 204565, 'Belarus': 47433, 'Iceland': 20047, 'Slovakia': 89552}, {'El Salvador': 6344722, 'Dominican Republic': 10648791, 'Guatemala': 16582469, 'Honduras': 9112867, 'Panama': 4034119, 'Papua New Guinea': 8084991, 'Australia': 24125848, 'Israel': 8191828, 'Cyprus': 1170125, 'Philippines': 103320222, 'Brunei': 423196, 'Saudi Arabia': 32275687, 'Kenya': 48461567, 'Cameroon': 23439189, 'Ghana': 28206728, 'Tunisia': 11403248, 'Rwanda': 11917508, 'Austria': 8712137, 'Portugal': 10371627, 'Belarus': 9480042, 'Iceland': 332474, 'Slovakia': 5444218}],
    ['Oceania', 1858913, {'Americas': ['Puerto Rico', 'Argentina', 'Barbados'], 'Oceania': ['Australia', 'Papua New Guinea', 'New Zealand', 'Fiji'], 'Asia': ['Mongolia', 'Thailand', 'Philippines', 'Macau'], 'Africa': ['Madagascar', 'Mauritania', 'Libya', 'Burundi', 'Lesotho'], 'Europe': ['Spain', 'Finland', 'Russia']}, {'Puerto Rico': 103135, 'Argentina': 545866, 'Barbados': 4588, 'Australia': 1204616, 'Papua New Guinea': 16929, 'New Zealand': 185017, 'Fiji': 4632, 'Mongolia': 11160, 'Thailand': 406840, 'Philippines': 304905, 'Macau': 44803, 'Madagascar': 9991, 'Mauritania': 4635, 'Libya': 29153, 'Burundi': 3007, 'Lesotho': 2200, 'Spain': 1237255, 'Finland': 236785, 'Russia': 1283162}, {'Puerto Rico': 3667903, 'Argentina': 43847430, 'Barbados': 284996, 'Australia': 24125848, 'Papua New Guinea': 8084991, 'New Zealand': 4660833, 'Fiji': 898760, 'Mongolia': 3027398, 'Thailand': 68863514, 'Philippines': 103320222, 'Macau': 612167, 'Madagascar': 24894551, 'Mauritania': 4301018, 'Libya': 6293253, 'Burundi': 10524117, 'Lesotho': 2203821, 'Spain': 46347576, 'Finland': 5503132, 'Russia': 143964513}],
    ['Americas', 320912, {'Americas': ['Guatemala', 'Uruguay', 'El Salvador', 'Venezuela'], 'Oceania': ['Australia', 'Papua New Guinea'], 'Asia': ['Bangladesh', 'Laos', 'Qatar', 'Singapore'], 'Africa': ['Chad', 'Senegal', 'Kenya', 'Cameroon'], 'Europe': ['Switzerland', 'Croatia']}, {'Guatemala': 68763, 'Uruguay': 52420, 'El Salvador': 26797, 'Venezuela': 371337, 'Australia': 1204616, 'Papua New Guinea': 16929, 'Bangladesh': 221415, 'Laos': 15903, 'Qatar': 152469, 'Singapore': 296966, 'Chad': 9601, 'Senegal': 14765, 'Kenya': 70529, 'Cameroon': 24204, 'Switzerland': 668851, 'Croatia': 50425}, {'Guatemala': 16582469, 'Uruguay': 3444006, 'El Salvador': 6344722, 'Venezuela': 31568179, 'Australia': 24125848, 'Papua New Guinea': 8084991, 'Bangladesh': 162951560, 'Laos': 6758353, 'Qatar': 2569804, 'Singapore': 5622455, 'Chad': 14452543, 'Senegal': 15411614, 'Kenya': 48461567, 'Cameroon': 23439189, 'Switzerland': 8401739, 'Croatia': 4213265}],
    ['Asia', 11927, {'Americas': ['Belize', 'Guatemala', 'Peru', 'Costa Rica', 'Mexico'], 'Oceania': ['Australia', 'Fiji', 'New Zealand'], 'Asia': ['South Korea', 'Tajikistan', 'Cambodia', 'Pakistan'], 'Africa': ['Ghana', 'Equatorial Guinea', 'Somalia', 'Malawi', 'Swaziland'], 'Europe': ['France', 'Czech Republic', 'Norway', 'Denmark', 'Croatia']}, {'Belize': 1765, 'Guatemala': 68763, 'Peru': 192094, 'Costa Rica': 57436, 'Mexico': 1046922, 'Australia': 1204616, 'Fiji': 4632, 'New Zealand': 185017, 'South Korea': 1411246, 'Tajikistan': 6952, 'Cambodia': 20017, 'Pakistan': 283660, 'Ghana': 42690, 'Equatorial Guinea': 10179, 'Somalia': 6217, 'Malawi': 5442, 'Swaziland': 3727, 'France': 2465453, 'Czech Republic': 192925, 'Norway': 370557, 'Denmark': 306143, 'Croatia': 50425}, {'Belize': 366954, 'Guatemala': 16582469, 'Peru': 31773839, 'Costa Rica': 4857274, 'Mexico': 127540423, 'Australia': 24125848, 'Fiji': 898760, 'New Zealand': 4660833, 'South Korea': 50791919, 'Tajikistan': 8734951, 'Cambodia': 15762370, 'Pakistan': 193203476, 'Ghana': 28206728, 'Equatorial Guinea': 1221490, 'Somalia': 14317996, 'Malawi': 18091575, 'Swaziland': 1343098, 'France': 64720690, 'Czech Republic': 10610947, 'Norway': 5254694, 'Denmark': 5711870, 'Croatia': 4213265}],
    ['Oceania', 27318, {'Americas': ['Ecuador', 'Bolivia', 'Paraguay'], 'Oceania': ['New Zealand', 'Australia'], 'Asia': ['Pakistan', 'Cambodia', 'Malaysia'], 'Africa': ['Mauritania', 'Lesotho'], 'Europe': ['Spain', 'Ukraine']}, {'Ecuador': 97802, 'Bolivia': 33806, 'Paraguay': 27441, 'New Zealand': 185017, 'Australia': 1204616, 'Pakistan': 283660, 'Cambodia': 20017, 'Malaysia': 296359, 'Mauritania': 4635, 'Lesotho': 2200, 'Spain': 1237255, 'Ukraine': 93270}, {'Ecuador': 16385068, 'Bolivia': 10887882, 'Paraguay': 6725308, 'New Zealand': 4660833, 'Australia': 24125848, 'Pakistan': 193203476, 'Cambodia': 15762370, 'Malaysia': 31187265, 'Mauritania': 4301018, 'Lesotho': 2203821, 'Spain': 46347576, 'Ukraine': 44438625}],
]
expected_return_values = [
    0,
    69419515,
    24125848,
    52334028,
    23439189,
    143787737,
    0,
    31568179,
    259757765,
    28786681,
]
print("############ Testing Part III ############")
for a, e in zip(args, expected_return_values):
    print('Testing sum_populations() with:\n\twhich_continent = {}\n'
          '\tmin_gdp = {}\n'
          '\tcountries = {}\n'
          '\tgdps = {}\n'
          '\tpopulations = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = sum_populations(*a)
    print('Actual Return Value:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[2] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part IV
args = [
    ['students1.txt', 'CSE220'],
    ['students1.txt', 'CSE114'],
    ['students1.txt', 'CSE475'],
    ['students1.txt', 'CSE219'],
    ['students1.txt', 'CSE214'],
    ['students2.txt', 'CSE219'],
    ['students2.txt', 'CSE214'],
    ['students2.txt', 'CSE220'],
    ['students2.txt', 'CSE114'],
    ['students2.txt', 'CSE101'],
    ['students3.txt', 'CSE220'],
    ['students3.txt', 'CSE101'],
    ['students3.txt', 'CSE219'],
    ['students3.txt', 'CSE114'],
    ['students3.txt', 'CSE214'],
]
expected_return_values = [
    ['110071435', '110071432', '110071434'],
    ['110071435', '110071434'],
    ['110071436', '110071435'],
    ['110071434', '110071432', '110071433'],
    ['110071433', '110071436'],
    ['110071438'],
    ['110071447', '110071450', '110071441', '110071442'],
    ['110071446', '110071449', '110071448'],
    ['110071449', '110071447', '110071444', '110071441', '110071448', '110071437'],
    ['110071437', '110071446'],
    ['110071434', '110071441', '110071438', '110071449', '110071439', '110071445', '110071435'],
    ['110071442', '110071438', '110071435', '110071448', '110071432'],
    ['110071435', '110071442', '110071446', '110071438', '110071437'],
    ['110071451', '110071441', '110071437', '110071435'],
    ['110071449', '110071440', '110071436'],
]

print("############ Testing Part IV ############")
for a, e in zip(args, expected_return_values):
    print('Testing get_roster() with filename = {}, course = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = get_roster(*a)
    print('Actual Return Value:   {}'.format(actual))
    if isinstance(actual, list):
        actual = sorted(actual)
    if sorted(e) == actual:
        print('Correct!')
        part_counts[3] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part V
args = [
    ['sundaes.txt', 'Topping', 'Flavor', 'RockyRoad'],
    ['sundaes.txt', 'Flavor', 'Size', 'Medium'],
    ['sundaes.txt', 'Syrup', 'Topping', 'WhippedCream'],
    ['sundaes.txt', 'Topping', 'Syrup', 'Fudge'],
    ['sundaes.txt', 'Syrup', 'Size', 'Small'],
    ['sundaes.txt', 'Flavor', 'Syrup', 'Caramel'],
    ['sundaes.txt', 'Size', 'Flavor', 'Vanilla'],
    ['sundaes.txt', 'Size', 'Topping', 'Sprinkles'],
    ['clothing.txt', 'Price', 'BodyType', 'Man'],
    ['clothing.txt', 'BodyType', 'BodyType', 'Girl'],
    ['clothing.txt', 'ClothingType', 'BodyType', 'Baby'],
    ['clothing.txt', 'ClothingType', 'BodyType', 'Woman'],
    ['clothing.txt', 'Manufacturer', 'Size', 'Small'],
    ['clothing.txt', 'Price', 'Size', 'XL'],
    ['clothing.txt', 'Manufacturer', 'ClothingType', 'Socks'],
    ['clothing.txt', 'BodyType', 'Size', 'Medium'],
    ['clothing.txt', 'Size', 'Manufacturer', 'Lee'],
    ['clothing.txt', 'Price', 'Manufacturer', 'Levi'],
    ['clothing.txt', 'Size', 'ClothingType', 'Jacket'],
    ['clothing.txt', 'BodyType', 'Price', '53'],
]
expected_return_values = [
    ['WhippedCream', 'WhippedCream', 'ChocolateChips', 'ChocolateChips', 'Sprinkles', 'WhippedCream', 'ChocolateChips', 'ChocolateChips', 'Sprinkles', 'Sprinkles', 'ChocolateChips'],
    ['Strawberry', 'RockyRoad', 'Strawberry', 'Vanilla', 'Strawberry', 'RockyRoad', 'Strawberry', 'Chocolate', 'Chocolate', 'Chocolate', 'Chocolate', 'RockyRoad', 'Strawberry', 'Vanilla', 'Chocolate', 'Vanilla'],
    ['Fudge', 'Fudge', 'Fudge', 'Fudge', 'Blueberry', 'Blueberry', 'Blueberry', 'Fudge', 'Blueberry', 'Caramel', 'Fudge', 'Caramel', 'Blueberry', 'Fudge', 'Caramel'],
    ['WhippedCream', 'WhippedCream', 'WhippedCream', 'WhippedCream', 'ChocolateChips', 'ChocolateChips', 'Sprinkles', 'Sprinkles', 'ChocolateChips', 'Sprinkles', 'WhippedCream', 'WhippedCream', 'ChocolateChips', 'WhippedCream', 'ChocolateChips'],
    ['Fudge', 'Caramel', 'Blueberry', 'Caramel', 'Blueberry', 'Blueberry', 'Blueberry', 'Fudge', 'Caramel', 'Fudge', 'Caramel', 'Blueberry', 'Caramel', 'Fudge', 'Caramel', 'Caramel', 'Caramel', 'Blueberry', 'Fudge'],
    ['Strawberry', 'Vanilla', 'RockyRoad', 'Strawberry', 'Strawberry', 'Chocolate', 'RockyRoad', 'Strawberry', 'Chocolate', 'Chocolate', 'Vanilla', 'Vanilla', 'RockyRoad', 'Strawberry', 'RockyRoad', 'Strawberry', 'Vanilla', 'Vanilla'],
    ['Large', 'Medium', 'Small', 'Small', 'Large', 'Small', 'Small', 'Large', 'Medium', 'Small', 'Medium'],
    ['Large', 'Medium', 'Small', 'Large', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Large', 'Large', 'Medium', 'Small', 'Small'],
    ['22', '23', '53', '42', '60', '24'],
    ['Girl', 'Girl', 'Girl', 'Girl', 'Girl', 'Girl', 'Girl'],
    ['Socks', 'Socks', 'Pants', 'Shirt', 'Jacket', 'Jacket', 'Socks', 'Socks', 'Jacket', 'Pants'],
    ['Pants', 'Socks', 'Coat', 'Pants', 'Coat', 'Coat', 'Pants'],
    ['Chanel', 'Aeropostale', 'Lee', 'Lee', 'Adidas', 'Levi', 'Lee', 'Lee', 'Aeropostale', 'Levi', 'Lee', 'Levi'],
    ['24', '42', '60', '60', '24'],
    ['Chanel', 'Lee', 'Levi', 'Levi', 'Levi', 'Lee'],
    ['Man', 'Woman', 'Boy', 'Baby', 'Girl', 'Girl', 'Baby', 'Boy', 'Baby', 'Girl'],
    ['XL', 'Small', 'Small', 'XXL', 'XXL', 'Large', 'Small', 'Small', 'Medium', 'Medium', 'Small', 'XL', 'Medium'],
    ['24', '42', '53', '60', '23', '60', '42', '53', '23', '24'],
    ['XL', 'Medium', 'XXL', 'XL', 'Medium', 'Small', 'Large'],
    ['Man', 'Boy', 'Baby', 'Girl'],
]
print("############ Testing Part V ############")
for a, e in zip(args, expected_return_values):
    print('Testing fetch_value() with filename = {}, selected_field = {}, '
          'searched_field = {}, searched_value = {}'.format(*a))
    print('Expected Return Value: {}'.format(e))
    actual = fetch_value(*a)
    print('Actual Return Value:   {}'.format(actual))
    if isinstance(actual, list):
        actual = sorted(actual)
    if sorted(e) == actual:
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
print(f'Part IV:  {part_counts[3]}/{test_counts[3]}')
print(f'Part V:   {part_counts[4]}/{test_counts[4]}')
