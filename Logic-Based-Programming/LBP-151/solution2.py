# Using Function

# Solution:

def sumOfDistance(L):
    sum = 0
    for i in range(0,len(L)-1):
        sum = sum + abs(L[i] - L[i+1])
    return sum

n = int(input())
L = [int(i) for i in input().split()]
print(sumOfDistance(L))
