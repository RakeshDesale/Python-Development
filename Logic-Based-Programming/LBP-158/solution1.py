# Solution:

def alternatePositiveNegative(L):
    flag = True
    for i in range(n-1):
        if ((L[i]>=0 and L[i+1]>=0) or (L[i]<0 and L[i+1]<0)):
            flag = False
            break
    return flag

n = int(input())
print(str(alternatePositiveNegative([int(i) for i in input().split()])).lower())
