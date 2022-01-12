# Solution:

n=int(input())
sum=0
if n>0:
    while n!=0:
        d=n%10
        if d==3 or d==6 or d==9:
            sum=sum+d
        n=n//10
    print (sum)
else:
    pass
