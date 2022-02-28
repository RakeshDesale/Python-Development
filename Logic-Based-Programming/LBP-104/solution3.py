# Using Function

# Solution:

def oddSum(L):
    sum = 0
    for i in L:
        if i%2!=0:
            sum = sum + i
    return sum

n = int(input())
print(oddSum([int(i) for i in input().split()]))
