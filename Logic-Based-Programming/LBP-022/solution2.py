# Solution:

n=int(input())
sum=0
temp=n
if n>0:
    while n!=0:
        d=n%10
        sum=sum+d
        n=n//10
    print('Yes' if temp%sum==0 else 'No')
else:
    pass
