# Using Function and Using Core Logic

# Solution:

def arrPali(L):
    flag = True
    low = 0
    high = n-1
    while low <= high:
        if L[low] != L[high]:
            flag = False
            break
        low += 1
        high -= 1
    return flag
    
n = int(input())
L = [int(i) for i in input().split()]
print(str(arrPali(L)).lower())
