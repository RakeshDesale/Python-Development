# Using Function

# Optimized Solution:

def oddSum(L):
    return sum([i for i in L if i%2!=0])

n = int(input())
print(oddSum([int(i) for i in input().split()]))
