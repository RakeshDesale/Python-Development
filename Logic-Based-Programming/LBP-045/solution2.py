# Without Using Function

# Solution:

n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i

print("true" if sum==n else "false")
