#  Using Function

# Solution:

def isPrime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    return factors == 2

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
sum = 0
for i in range(3):
    for j in range(3):
        if isPrime(L[i][j]):
            sum = sum + L[i][j]
print(sum)
