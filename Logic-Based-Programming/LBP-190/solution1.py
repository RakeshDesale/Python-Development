# Solution:

L = [int(i) for i in input()]
L.sort()
flag = True
for i in range(len(L)-1):
    if(abs(L[i] - L[i+1]) > 2):
        flag = False
        break
print("Yes" if flag else "No")
