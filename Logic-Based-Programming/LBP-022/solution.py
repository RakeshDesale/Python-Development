# Solution:

n=int(input())
sum=0
temp=n
if n>0:
    while n!=0:
        d=n%10
        sum=sum+d
        n=n//10
    if temp%sum==0:
        print ('Yes')
    else:
        print ('No')
else:
    pass
