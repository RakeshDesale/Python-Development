# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
for i in range(n):
    if L[i]>0:
        print(L[i]+L[i+1])
        break
