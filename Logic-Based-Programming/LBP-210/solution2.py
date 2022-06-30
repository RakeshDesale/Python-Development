# Using Function

# Solution:

def sumFirstLast(L):
    return L[0][0] + L[2][2]

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(sumFirstLast(L))
