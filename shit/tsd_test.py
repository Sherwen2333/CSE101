import random
z='@Instance'
g='label'
# print(random.random)
for i in range(20):
    i=str(i)
    f1=int(100*random.random())
    f2=int(100*random.random())
    f1/=10
    f2/=10
    print(z+i+'\t'+g+str(1)+'\t'+str(f1)+','+str(f2))