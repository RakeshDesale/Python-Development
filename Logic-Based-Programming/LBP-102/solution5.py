# Another Approach Using Function

# Solution:

def sumArray(L):
    sum = 0
    for i in L:
        sum = sum+i
    return sum

n = int(input())
print(sumArray([int(i) for i in input().split()]))
