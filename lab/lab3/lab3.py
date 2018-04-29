# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 3


# Part I
def sanitize(st):
    res=["","",""]
    for i in st:
        if str(i).isupper():res[0]+=(i)
        if str(i).islower():res[1]+=(i)
        if str(i).isdigit():res[2]+=(i)
    return res


# Part II
def party(prices, shopping_list):
    pizza=0
    soda=0
    cost=0
    for i in shopping_list:
        if i =='pizza':
            pizza+=1
        elif i=='soda':
            soda+=1
        elif i=='cup':
            cost+=prices[1]
        elif i=='plate':
            cost+=prices[2]
    if soda>=5:
        cost+=soda*prices[3]*0.92
    else:
        cost+=soda*prices[3]
    if pizza==2:
        cost+=pizza*prices[0]
        cost*=0.9
    elif  pizza>2:
        cost+=pizza*prices[0]
        cost*=0.8
    else:cost+=pizza*prices[0]
    return cost


# Part III
# Fix broken code
def school_dilemma(age):
    if age < 6:
        return 'Too young for school'
    elif 6 <= age < 11:
        return 'Elementary school'
    elif 11 <= age < 14:
        return 'Middle school'
    elif 14 <= age < 18:
        return 'High school'
    elif age >= 18:
        return 'College'
    else:
        return None
