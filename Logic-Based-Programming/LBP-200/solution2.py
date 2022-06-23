# Using Function

# Solution:

def sumOfRemainder(L,k):
    sum = 0
    for i in L:
        sum = sum + i % k
    return sum

n = int(input())
L = [int(i) for i in input().split()]
print(sumOfRemainder(L,int(input())))
