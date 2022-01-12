# Solution:

n=int(input())
sum=0
if n>0:
    while n!=0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:
            sum=sum+d
        n=n//10
    print (sum)
else:
    pass
