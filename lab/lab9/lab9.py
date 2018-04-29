# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 9


# Part I
def search_log(log_messages, user, message_type):
    res=[]
    for i in log_messages:
        z= str(i).split(';')
        if z[1]==user and z[2]==message_type:
            res.append(z[1]+'>'+z[3])
    return res


# Part II
def encode_steps(message):
    if len(message)==1:
        return message
    else:
        z=[]
        res=[]
        for i in message:
            z.append(ord(i))
        for i in range(len(z)-1):
            res.append(z[i+1]-z[i])
        message=list(message)
        asd=''
        for i in range(len(message)):
            asd+=message[i]
            if i < len(res):
                asd+=str(res[i])
    return asd
