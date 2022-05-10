# Using Function

# Solution:

def countUnchanged(L1):
    L2 = L1.copy()
    L1.sort()
    count = 0
    for i in range(n):
        if L1[i] == L2[i]:
            count += 1
    return count

n = int(input())
print(countUnchanged([int(i) for i in input().split()]))
