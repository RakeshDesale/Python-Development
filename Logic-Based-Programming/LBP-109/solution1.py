# Solution:

n=int(input())
L=[int(i) for i in input().split()]
key=int(input())
index=-1
for i in range(0,len(L)):
    if L[i]==key:
        index=i
        break
print(index)
