# Another Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
key = int(input())
index=-1
for i in range(0,len(L)):
    for j in range(i+1,len(L)):
        if(L[i] > L[j]):
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

if key in L:
    print(L.index(key))
else:
    print(-1)
