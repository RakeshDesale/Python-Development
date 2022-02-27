# Using Function

# Optimized Solution:

def evenSum(L):
    return sum([i for i in L if i%2==0])

n = int(input())
L = [int(i) for i in input().split()]
print(evenSum(L))
