# Using Function

# Solution:

def sumOfProd(a):
    sum = 0
    for i in a:
        sum = sum + (i * (i + 1))
    return sum

n = int(input())
print(sumOfProd([int(i) for i in input().split()]))
