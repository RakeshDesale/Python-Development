# Using Function

# Solution:

def countZero(L):
    counter = 0
    for i in L:
        counter = counter + i.count(0)
    return counter >= 5

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
print("Yes" if countZero(L) else "No")
