# Solution:

numMsg=int(input())
sum=0
while numMsg!=0:
    d=numMsg%10
    if d==1 or d==2 or d==3 or d==5 or d==7:
        pass
    else:
        sum=sum+d
    numMsg=numMsg//10
print(sum)
