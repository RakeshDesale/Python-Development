# Solution:

def isPrime(n):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    return factors==2

n = int(input())
L = [int(i) for i in input().split()]
count = 0
for i in L:
    if (isPrime(i)):
        count+=1
print("true" if count==n else "false")
