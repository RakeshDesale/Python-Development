# Core Concept Using Function

# Solution:

def eleCount(L,key):
    count = 0
    for i in L:
        if i==key:
            count+=1
    return count

n = int(input())
L = [int(i) for i in input().split()]
print(eleCount(L,int(input())))
