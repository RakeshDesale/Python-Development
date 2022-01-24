# Solution:

n=int(input())
sum=0
while n!=0:
    d=n%10
    if d==4 or d==6 or d==8 or d==9:
        sum=sum+d
    n=n//10
print (sum)
