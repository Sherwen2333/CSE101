# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Homework 3



# Part I
def frog(mood, actions):
    result=mood
    for i in actions:
        if i is 'play':
            result+=3
        elif i is 'eat':
            if result>=0.5*mood:
                result+=1
            else:result-=2
        elif i is 'read':
            if result>=0.75*mood:
                result-=3
            else:result-=4
        elif i is 'work':
                result-=5
        result-=1
    if result>0:return result
    return 0


# Part II
def pacman(line):
    ghost=list('ghostGHOST')
    for i in range(len(line)):
        if line[i] not in ghost:
            line[i]='_'
            if i==len(line)-1:
                line.append('<')
        else:
            if i==0:
                line=['<']+line

            else:line[i-1]='<'
            break
    return line


# Part III
def brackets(expr):
    left=[]
    a=dict(zip(list('{[('),list('}])')))
    b=dict(zip(list('}])'),list('{[(')))

    for i in expr:
        if i in a.keys():
            left.append(i)
        elif i in a.values() and len(left) is 0:
            return 'error'
        elif i in a.values() and left[len(left)-1]==b[i]:
            left.pop()
        else:return left
    return left


# Part IV
def hail_length(n):
    a=1
    while n!=1:
        if n%2==0:
            n//=2
        else:n=n*3+1
        a+=1
    return a


def siblings(length, maximum):
    result=[]
    for i in range(1,maximum+1):
        if hail_length(i)==length:
            result.append(i)
    return result


# Part V
def vampire_hunt(humans, vampires, hunters):
    # humans=84
    # vampires=6
    # hunters=2
    while humans>0 and vampires>0:
        if vampires>=hunters:
            vampires-=hunters
        else:vampires-=vampires
        a=humans
        if humans>=vampires:
            humans-=vampires
        else:humans-=humans
        vampires+=(a-humans)
    return [humans,vampires]
