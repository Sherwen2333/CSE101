# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 10

from package import *


# Part I
def shipping_cost(packages, cost_schedule):
    cost=0
    for i in packages:
        if i.distance<=100:
            i.cost=cost_schedule[0]
        elif 100<=i.distance<300:
            i.cost=cost_schedule[1]
        elif 300 <= i.distance < 500:
            i.cost = cost_schedule[2]
        else:
            i.cost = cost_schedule[3]
        cost+=i.cost
    return cost


# Part II
def package_tracking(packages_info, locations, cost_schedule):
    res=[]
    for i in packages_info:
        distance=((locations[i[0]][0]-locations[i[1]][0])**2+(locations[i[0]][1]-locations[i[1]][1])**2)**0.5
        package=Package(i[0], i[1], cost=0, distance=distance)
        res.append(package)
    shipping_cost(res, cost_schedule)
    return res
