# Another Way Using Function

# Solution:

def secondMin(L):
    L = sorted(L)
    return L[2-1]

n = int(input())
print(secondMin([int(i) for i in input().split()]))
