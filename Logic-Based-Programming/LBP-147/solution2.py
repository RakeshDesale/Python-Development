# Another Approach

# Solution:

n = int(input())
L = sorted([int(i) for i in input().split()])
for i in range(n):
    if L[i]>0:
        print(L[i]+L[i+1])
        break
