# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 6


# Part I
def student_alert(students):
    grade={'A':95,'B':85,'C':75,'D':65,'F':55}
    res=[]
    for i in students:
        avg=0
        for z in i:
            avg+=grade[z]
        avg/=len(i)
        if avg<70:
            res.append('R')
        elif avg<80:
            res.append('Y')
        else:
            res.append('G')
    return res


# Part II
def find_employee(employees, search_field, search_value):
    res=[]
    for i in employees:
        found=False;
        name=''
        for z in i:
            if z[0]==search_field and z[1]==search_value:
                found=True
            if z[0]=='Name':
               name=z[1]
        if found is True:
            res.append(name)
    return res
