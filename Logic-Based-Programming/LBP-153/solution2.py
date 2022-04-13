# Using Function

# Solution:

def numberOfPlots(L):
    count = 0
    for i in range(n):
        for j in range(1,L[i]+1):
            if j*j==L[i]:
                count += 1
    return count

n = int(input())
print(numberOfPlots([int(i) for i in input().split()]))
