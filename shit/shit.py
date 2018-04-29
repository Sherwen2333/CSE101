import math
def c(a,b):
    print(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
c(9,4)
c(9,5)
def f(a):
    return math.factorial(a)
print(f(9)/(f(2)*f(2)*f(2)))