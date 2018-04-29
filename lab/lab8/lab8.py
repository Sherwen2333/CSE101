# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 8


# Part I
def vacation_calculator(room_prices, budget, reservations):
    cost=0
    cost_list=[]
    for i in reservations:
        if budget-room_prices[i[0]]*i[1]>0:
            budget-=room_prices[i[0]]*i[1]
            cost+=room_prices[i[0]]*i[1]
            cost_list.append(i)
    return cost, cost_list


# Part II
def hotel_manager(room_prices, room_counts, reservations):
    cost=0
    cost_list={}
    for i in reservations:
        if room_counts[i[0]]-i[1]>=0:
            cost+=room_prices[i[0]]*i[1]
            room_counts[i[0]]-=i[1]
            if i[0] in cost_list.keys():
                cost_list[i[0]]+=room_prices[i[0]]*i[1]
            else:
                cost_list[i[0]] = room_prices[i[0]] * i[1]
    return cost, cost_list
