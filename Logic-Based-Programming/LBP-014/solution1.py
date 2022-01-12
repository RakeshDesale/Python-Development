# Using Standard Mathematical Formula

# Solution:

n=int(input())
rev=0
if n>=0:
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev)
else:
    pass
