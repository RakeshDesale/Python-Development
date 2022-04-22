# Using Core Logic

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
flag = True
low = 0
high = n-1
while low <= high:
    if L[low] != L[high]:
        flag = False
        break
    low += 1
    high -= 1
print(str(flag).lower())
