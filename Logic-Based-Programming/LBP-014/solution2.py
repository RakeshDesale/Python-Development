# Solution:

n=int(input())
if n>=0:
    if n==0:
        print(n)
    else:
        while n!=0:
            d=n%10
            print(d,end='')
            n=n//10
else:
    pass
