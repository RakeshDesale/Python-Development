# Solution:

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def numberOfWays(n):
    return fib(n+1)

print(numberOfWays(int(input())))
