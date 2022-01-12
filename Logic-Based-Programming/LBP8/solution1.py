# Solution:

n=int(input())
sum=0
if (n>0):
    while n!=0:
        d=n%10
        sum+=d
        n=n//10
    print(sum)
else:
    pass
