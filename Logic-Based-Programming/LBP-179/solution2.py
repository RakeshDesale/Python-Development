# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L1 = []
L2 = []
L.sort()
for i in L:
    if i%2==0:
        L1.append(i)
    else:
        L2.append(i)
index = 0
while index<n//2:
    print(L1[index],L2[index],end=' ')
    index += 1
