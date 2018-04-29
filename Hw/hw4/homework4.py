# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Homework 4

# Part I
def password_strength(password):
    res=0
    for i in range(len(password)):
        if i ==0:
            if str(password[i]).isdigit():
                res+=40
            elif str(password[i]).isupper():
                res+=25
            elif str(password[i]).islower():
                res+=5
            else:
                res+=25
        if i==(len(password)-1):
            if str(password[i]).isdigit():
                res+=50
            elif str(password[i]).islower() and len(password)!=1:
                res+=5
            elif str(password[i]).islower() and len(password)==1:
                res+=0
            elif str(password[i]).isupper():
                res+=15
            else:
                res+=35
        if i!=0 and i!=(len(password)-1):
            if str(password[i]).isdigit():
                res+=25
            elif str(password[i]).isupper():
                res+=10
            elif str(password[i]).islower():
                res+=5
            else:res+=15
    return res*len(password)

# Part II
def order_lunches(stock, orders):
    ak=0
    for i in orders:
        if i in dict(stock).keys():
            if stock[i]>0:
                stock[i]-=1
                ak+=1
    return ak

# Part III
def sum_populations(which_continent, min_gdp, countries, gdps, populations):
    sum=0
    for i in countries[which_continent]:
        if gdps[i]>=min_gdp:
            sum+=populations[i]
    return sum

# Part IV
def get_roster(filename, course):
    res=[]
    for i in open(filename):
        z=str(i).split(',')
        if z[2]==course:
            res.append(z[1])
    return res

# Part V
def fetch_value(filename, selected_field, searched_field, searched_value):
    search={}
    res=[]
    for i in open(filename):
        z=i.replace('\n','').split(',')
        if len(search.keys())==0:
            for i in range(len(z)):
                search[z[i]]=i
            print(search)
        if z[search[searched_field]]==searched_value:
            res.append(z[search[selected_field]])
    return res
