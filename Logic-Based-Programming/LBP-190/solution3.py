# Using Core Logic

# Solution:

L = [int(i) for i in input()]
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i] > L[j]:
            L[i],L[j] = L[j],L[i]
flag = True
for i in range(len(L)-1):
    if(abs(L[i] - L[i+1]) > 2):
        flag = False
        break
print("Yes" if flag else "No")
