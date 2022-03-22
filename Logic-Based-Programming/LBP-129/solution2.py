# Using Function

# Solution:

def duplicateElements(L):
    d = {}
    count = 0
    for i in L:
        d[i] = d.get(i,0)+1
    for i in d.values():
        if i>=2:
            count+=1
    return count

n = int(input())
print(duplicateElements([int(i) for i in input().split()]))
