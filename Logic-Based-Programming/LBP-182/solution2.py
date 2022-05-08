# Using Function

# Solution:

def isPrime(n):
    factors = 0
    for i in range(1,n+1):
        if n%i == 0:
            factors += 1
    return factors == 2

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
L1 = []
for i in L:
    if isPrime(i):
        L1.append(i)
L1.sort()
if len(L1)>=2:
    print(abs(L1[len(L1)-1] - L1[0]))
else:
    print(0)
