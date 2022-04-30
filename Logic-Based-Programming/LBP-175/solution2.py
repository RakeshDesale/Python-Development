# Using Function

# Solution:

def isPrime(n):
    factors = 0
    for i in range(1,n+1):
        if n%i == 0:
            factors += 1
    return factors == 2

n = int(input())
for i in range(2,n+1):
    if isPrime(i):
        print(i,end=' ')
