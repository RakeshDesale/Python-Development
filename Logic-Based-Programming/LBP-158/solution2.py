# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
flag = True
for i in range(n-1):
    if ((L[i]>=0 and L[i+1]>=0) or (L[i]<0 and L[i+1]<0)):
        flag = False
        break
print(str(flag).lower())
