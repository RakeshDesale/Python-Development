# Another Way Using Function

# Solution:

def isPrime(n):
    factors=0
    for i in range (1,n+1):
        if n%i==0:
            factors+=1
    print(str(factors==2).lower())
    
isPrime(int(input()))
