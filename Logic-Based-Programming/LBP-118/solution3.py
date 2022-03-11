# Optimized Way Using Function

# Solution:

def eleCount(L,key):
    return L.count(key)

n = int(input())
L = [int(i) for i in input().split()]
print(eleCount(L,int(input())))
