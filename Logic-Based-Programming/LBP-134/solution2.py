# Using Function

# Solution:

def evenLocSum(L):
    sum = 0
    for i in range(len(L)):
        if i%2==0:
            sum = sum + L[i]
    return sum

n = int(input())
print(evenLocSum([int(i) for i in input().split()]))
