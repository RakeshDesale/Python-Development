# Solution:

n=int(input())
sumeven=0
sumodd=0

while n!=0:
    d=n%10
    if d%2==0:
        sumeven+=d
    else:
        sumodd+=d
    n=n//10

print(sumeven*sumodd)
