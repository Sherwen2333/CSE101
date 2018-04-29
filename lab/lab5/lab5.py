# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 5

def fizz_buzz(max_fizz_buzz, fizz, buzz):
    result = []
    counter = 0
    i = 1
    while max_fizz_buzz != counter:
        if i % fizz == 0 and i%buzz==0:
            result.append("fizzbuzz")
            counter += 1
        elif i % fizz == 0:
            result.append("fizz")
        elif i % buzz == 0:
            result.append("buzz")
        else:
            result.append(i)
        i += 1
    return result


def mass_purchase(city, budget):
    result=[]
    for i in range(len(city)):
        for z in range(len(city[i])):
            if budget>=city[i][z]:
                budget-=city[i][z]
                result.append([i,z])
    return result
