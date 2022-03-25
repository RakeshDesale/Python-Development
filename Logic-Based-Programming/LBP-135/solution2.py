# Using Function

# Solution:

def oddLocSum(L):
    sum = 0
    for i in range(len(L)):
        if i%2!=0:
            sum = sum + L[i]
    return sum

n = int(input())
print(oddLocSum([int(i) for i in input().split()]))
