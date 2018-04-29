import sys

student_file = 'lab13.py'

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
test_counts = [8, 11, 10]

from lab13 import *

# Testing Part I
args = [
    [['58 Gnarled Oak Street', '12 Chirping Bird Road', '173 East Main Road Apt. Q', '194 Sheep Street Apt. W']],
    [['Main Street', '12 Main Drive', '5 Elm', '6 Elm Apt. 5', '11 Elm Street Apt.', '6 main Street', '19 Dark Horse street']],
    [['12 Main Road', '12 Main Drive Apt. G', '100 Circle Road', '5 Elm', '6 Elm Road Apt. G', '12 Elm Street Apt. X', '44 Dark Hollow Road', '6 main Street', '19 Dark Horse street']],
    [['4 High ', '5 GNARLED OAK ROAD', '4 Chirping Bird Path', '57 Soaring Bald Eagle Path', '98 Gnarled Oak Road', '29 Street Apt. b', '28 SHEEP PATH APT. Y', '31 Gnarled Oak Road Apt. B', '52 GNARLED OAK PATH APT. S']],
    [['56 SHEEP PATH APT. P', '67 STREET', 'East Main Path Apt. h', '11 Sheep Street Apt. y', '83 GNARLED OAK ROAD', 'Road', '10 High Path Apt. f', '89 Street Apt. f', '55 east main street']],
    [['34 Soaring Bald Eagle Street', '98 Dark Elm Street Apt. m', '40 East Main  Apt. Y', '96 East Main ', '51 Road', '54 Gnarled Oak Path Apt. o', '15 Apple Path Apt. h', '56 Apple Path', '66 Apple Path', 'Dark Elm Street Apt. a', '82 Street Apt. A', '42 Soaring Bald Eagle Road']],
    [['97 apple street', 'Chirping Bird Street Apt. g', '26 Path Apt. n', '92 East Main Street', '73 Gnarled Oak Street', '42 DARK ELM PATH APT. H', '14 Chirping Bird Road Apt. Z', '59 Dark Elm ']],
    [['IUhwiV', 'FCaXcjUg', 'JEwrdGDrZocSKIn', 'QTkTNbin', 'TdiuIQev']],
]
expected_return_values = [
    [0, 1, 2, 3],
    [],
    [0, 2, 4, 5, 6],
    [2, 3, 4, 7],
    [],
    [0, 7, 8, 11],
    [3, 4, 6],
    [],
]

print("############ Testing Part I ############")
for a, e in zip(args, expected_return_values):
    print('Testing street_addresses() with addresses = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = street_addresses(*a)
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
    ['898-524-G0', {'898': 'Kuwait', '312': 'Russia', '709': 'Bangladesh', '400': 'Slovenia', '905': 'Yemen', '256': 'Slovakia', '085': 'Burundi'}],
    ['787-195-F5', {'167': 'Peru', '873': 'Brazil', '539': 'Greece', '787': 'Mongolia'}],
    ['328-168-I4', {'328': 'Equatorial Guinea', '378': 'Malawi', '319': 'Hungary', '612': 'Liberia', '839': 'Dominican Republic', '565': 'Mongolia', '036': 'Zimbabwe', '620': 'Luxembourg', '766': 'Panama', '562': 'India', '976': 'New Zealand', '904': 'Egypt', '603': 'Nepal', '013': 'Lebanon', '863': 'France'}],
    ['911-361-N2', {'991': 'Italy', '130': 'Jamaica', '380': 'Greece', '626': 'Qatar', '788': 'Slovenia', '126': 'Oman', '504': 'Zambia', '430': 'Rwanda', '911': 'Honduras', '355': 'Colombia', '796': 'Lithuania'}],
    ['861-135-H6', {'160': 'Equatorial Guinea', '259': 'Faroe Islands', '328': 'Democratic Republic of the Congo', '861': 'South Sudan'}],
    ['162-855-N9', {'921': 'Peru', '696': 'Uzbekistan', '571': 'Kyrgyzstan', '273': 'Chile', '164': 'Ghana', '349': 'Nigeria', '478': 'Bulgaria', '603': 'Paraguay', '642': 'Bahrain', '301': 'Turkmenistan', '863': 'Czech Republic', '126': 'Burkina Faso', '155': 'Iraq', '554': 'Laos', '907': 'Israel'}],
    ['11-456-W5', {'331': 'Libya', '664': 'Fiji', '229': 'Cape Verde', '002': 'Albania', '449': 'Hungary', '278': 'Turkey', '328': 'Niger', '633': 'Togo', '558': 'Lesotho', '861': 'Jordan', '251': 'Spain', '403': 'Algeria', '809': 'Chad'}],
    ['752-9194-M0', {'752': 'Sri Lanka', '815': 'Fiji', '141': 'Bulgaria', '992': 'Jamaica', '915': 'Lebanon', '903': 'Mali', '671': 'Central African Republic', '929': 'Uzbekistan', '893': 'Costa Rica', '197': 'Equatorial Guinea', '443': 'Brazil', '382': 'Burkina Faso', '650': 'Hong Kong'}],
    ['595-37-V1', {'595': 'Kyrgyzstan', '516': 'Spain', '310': 'Singapore', '391': 'Zimbabwe', '211': 'Austria', '081': 'Uruguay', '215': 'Sri Lanka', '640': 'Qatar', '218': 'Italy', '817': 'Georgia', '356': 'Sri Lanka'}],
    ['102-052-0', {'569': 'Fiji', '865': 'Denmark', '199': 'Bhutan', '951': 'Tanzania', '460': 'Rwanda', '046': 'Kenya', '340': 'Guyana', '922': 'Morocco', '416': 'Niger', '102': 'Andorra', '161': 'Lithuania', '921': 'Turkmenistan', '066': 'Togo', '593': 'Equatorial Guinea', '436': 'Egypt'}],
    ['382-525-N', {'151': 'Bhutan', '107': 'Jamaica', '991': 'Poland', '089': 'Japan', '382': 'Turkey', '427': 'Iceland', '276': 'New Zealand', '859': 'South Sudan', '613': 'Guyana', '170': 'Papua New Guinea'}],
]
expected_return_values = [
    'Kuwait',
    'Mongolia',
    'Equatorial Guinea',
    'Honduras',
    'South Sudan',
    'error',
    'error',
    'error',
    'error',
    'error',
    'error',
]

print("############ Testing Part II ############")
for a, e in zip(args, expected_return_values):
    print('Testing package_destination() with\n'
          '   package_code = {}\n'
          '   country_codes = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = package_destination(*a)
    print('Actual:   {}'.format(actual))
    if e == actual:
        print('Correct!')
        part_counts[1] += 1
    else:
        print('Incorrect!')
print('########################################')
print()


# Testing Part III
args = [
    ['*N Kaitlin Mcneill *P 2214595465 *T '],
    ['*N Dennis Mata P 3252274016 *T Claims Adjuster'],
    ['*N Milana Howser Ross *P 2214595465 *T Systems Administrator'],
    ['*N *P 0500932536 *T Investor Relations Officer'],
    ['*N Junior Senior Pickle Spears *P 6104177342 * Hedge Fund Trader'],
    ['*N Milana Howser Ross *P 4576100913 *T Digital Marketing Manager'],
    ['*N Junior Senior Pickle Spears * 8754171872 *T Insurance Investigator'],
    ['*N Eugene Gillespie *P 4576100913 *T Employee Relations Specialist'],
    ['*N Anisa Haines P 6899935115 *TWeb Developer'],
    ['*N Shaurya Nguyen *P 3252274016 *T Insurance Appraiser'],
]
expected_return_values = [
    'error',
    'error',
    'Name: Milana Howser Ross, Title: Systems Administrator, Phone: (221) 459-5465',
    'error',
    'error',
    'Name: Milana Howser Ross, Title: Digital Marketing Manager, Phone: (457) 610-0913',
    'error',
    'Name: Eugene Gillespie, Title: Employee Relations Specialist, Phone: (457) 610-0913',
    'error',
    'Name: Shaurya Nguyen, Title: Insurance Appraiser, Phone: (325) 227-4016',
]

print("############ Testing Part III ############")
for a, e in zip(args, expected_return_values):
    print('Testing business_card() with contact_info = {}'.format(*a))
    print('Expected: {}'.format(e))
    actual = business_card(*a)
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
