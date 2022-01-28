# Using Function

# Solution:

def isPrime(n):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    return factors==2

rl=int(input())
rr=int(input())
sum=0
for i in range(rl,rr+1):
    if(isPrime(i)):
        sum=sum+i
print(sum)
