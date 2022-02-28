# Using Function

# Solution:

def isPrime(n):
    factors=0
    for i in range(1,n+1):
        if(n%i==0):
            factors+=1
    return factors==2
    
n = int(input())
l = [int(i) for i in input().split()]
sum = 0
for i in l:
    if isPrime(i):
        sum = sum + i
print(sum)
