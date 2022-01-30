# Using While Loop

# Solution:

def isPrime(n):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    return factors==2

n=int(input())
while True:
    if isPrime(n):
        print(n)
        break
    n+=1
