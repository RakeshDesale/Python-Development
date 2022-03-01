# Using Function

# Optimized Solution:

def sortArrAsc(l):
    return sorted(l)

n = int(input())
l=(sortArrAsc([int(i) for i in input().split()]))
for i in l:
    print(i,end=' ')
