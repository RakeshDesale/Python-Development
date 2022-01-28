# Solution:

n=int(input())
prod=1
while n!=0:
    d=n%10
    prod*=d
    n=n//10
print(prod)
