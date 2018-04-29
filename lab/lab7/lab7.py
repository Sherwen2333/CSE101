# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 7

# Part I
def rec_hailstone_length(n):
    if n==1:return 1
    if n%2==0:return 1+rec_hailstone_length(n//2)
    return 1+rec_hailstone_length(n*3+1)


# Part II
def rec_work_cost(work_orders, hourly_costs):
    if len(work_orders)==0:return 0
    if work_orders[0][1:]=='pipe':return int(work_orders[0][0])*hourly_costs[0]+rec_work_cost(work_orders[1:],hourly_costs)
    if work_orders[0][1:]=='window':return int(work_orders[0][0])*hourly_costs[1]+rec_work_cost(work_orders[1:],hourly_costs)
    if work_orders[0][1:]=='sprinkler':return int(work_orders[0][0])*hourly_costs[2]+rec_work_cost(work_orders[1:],hourly_costs)