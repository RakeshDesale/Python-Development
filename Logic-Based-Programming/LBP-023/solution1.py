# Solution:

n=int(input())
sum=res=0
prod=1
if n>=10 and n<=99:
    temp=n
    while n!=0:
        d=n%10
        sum+=d
        prod*=d
        n=n//10
    res=sum+prod
    if temp==res:
        print("Yes")
    else:
        print("No")
else:
    pass
