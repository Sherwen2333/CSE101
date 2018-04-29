# Zhaowen Huang
# Zhaowhuang
# 111067886
# CSE 101
# Homework 1


# Part I
def compute1(x, y):
    return x / (y - 3 * x) + (x - 1) / (y / (x + 1))


# Part II
def farmhouse(W, L, H, P):
    return ((P - H) * 0.5 * W + W * H) * L


# Part III
def fuel(minutes, mph, mpg):
    return (minutes / 60 * mph) / mpg
