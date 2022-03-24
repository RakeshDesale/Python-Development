# Another Approach Using Function

# Solution:

def arrSort(L):
    return sorted([i for i in L])

n = int(input())
L = arrSort([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
