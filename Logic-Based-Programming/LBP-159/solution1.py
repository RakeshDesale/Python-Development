# Solution:

def allParamTrue(L):
    return 0 not in L

n = int(input())
print(str(allParamTrue([int(i) for i in input().split()])).lower())
