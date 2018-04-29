# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 11


# Part I
def compress_line(line):
    line=line.replace('\r','')
    line=line.replace('\n','')
    res=''
    z=''
    k=1
    for i in line:
        if z!=i :
            res+=str(k)+z
            z=i
            k=1
        else:
            k+=1
    # if res[-2]=='1' and (res[-1]=='\r' or res[-1]=='\n'):
    #     return res[1:-2]

    return res[1:]+str(k)+z


# Part II
def compress_file(filename):
    res=[]
    for i in open(filename):
        res.append(compress_line(i))
    return res