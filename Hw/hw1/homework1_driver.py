from homework1 import *

# Part I Tests

x = 6
y = -3
print('Testing compute1() with x = {}, y = {}: {}'.format(x, y, compute1(x, y)))
x = 93.33
y = 15
print('Testing compute1() with x = {}, y = {}: {}'.format(x, y, compute1(x, y)))
x = 4
y = 5.3
print('Testing compute1() with x = {}, y = {}: {}'.format(x, y, compute1(x, y)))

print()

# Part II Tests
W = 6.25
L = 17
H = 8
P = 9.7
print('Testing farmhouse() with W = {}, L = {}, H = {}, P = {}: {}'.\
      format(W, L, H, P, farmhouse(W, L, H, P)))
W = 19
L = 28
H = 10
P = 12
print('Testing farmhouse() with W = {}, L = {}, H = {}, P = {}: {}'.\
      format(W, L, H, P, farmhouse(W, L, H, P)))
W = 10
L = 40.5
H = 11
P = 16
print('Testing farmhouse() with W = {}, L = {}, H = {}, P = {}: {}'.\
      format(W, L, H, P, farmhouse(W, L, H, P)))

print()

# Part III Tests
minutes = 75
mph = 35.2
mpg = 20.6
print('Testing fuel() with mintues = {}, mph = {}, mpg = {}: {}'.\
      format(minutes, mph, mpg, fuel(minutes, mph, mpg)))

minutes = 60
mph = 60
mpg = 30
print('Testing fuel() with mintues = {}, mph = {}, mpg = {}: {}'.\
      format(minutes, mph, mpg, fuel(minutes, mph, mpg)))

minutes = 164.3
mph = 45.2
mpg = 19.41
print('Testing fuel() with mintues = {}, mph = {}, mpg = {}: {}'.\
      format(minutes, mph, mpg, fuel(minutes, mph, mpg)))