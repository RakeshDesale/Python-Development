# Solution:

n=int(input())
if n>=10 and n<=99:
    a=n%10
    b=(n//10)%10
    c=(a+b)+(a*b)
    print("Yes" if c==n else "No")
else:
    pass
