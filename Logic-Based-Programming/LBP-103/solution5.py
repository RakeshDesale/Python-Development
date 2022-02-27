# Another Optimized Approach Using Function

# Solution:

def evenSum(L):
    return sum([i for i in L if i%2==0])

n = int(input())
print(evenSum([int(i) for i in input().split()]))
