# Solution:

n=int(input())
if n>0:
    while n!=0:
        d=n%10
        print(d,end=' ')
        n=n//10
