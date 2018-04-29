# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Homework 2


# Part I
def summation(x, y):
    result=0
    for z in range (x,y+1):
        result+=((z*z*z-1)+(5*z-10)/3)
    return result


# Part II
def gas_reward(current_points, gas_type, money_spent):

    if current_points<0: return 'error'
    if money_spent <1:return current_points
    if gas_type =='Regular':gas_amount=money_spent/2.65
    elif gas_type =='Plus':gas_amount=money_spent/2.90
    elif gas_type =='Premium':gas_amount=money_spent/3.10
    else:return 'unavailable'
    if gas_amount<10: return current_points+int(money_spent)*5
    elif 15>gas_amount>=10: return current_points+200
    elif 20>gas_amount>=15: return current_points+400
    elif gas_amount>=20: return current_points+550


# Part III
def pull(strings, i):
    result =[]
    for z in strings:
        if i<len(z):
            result.append(z[i])
    return result


# Part IV
def print_cost(task):
    return task[2]*({'Letter':0.05,'Legal':0.06,'A4':0.055,'A5':0.04}[task[0]]+{'Gray Scale':0.01,'Colored':0.10}[task[1]])


# Part V
def total_cost(ID, tasks):
    total=0
    for i in tasks:
        if i[0]==ID:
            total+=print_cost(i[1:])
    return total
