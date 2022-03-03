# Using Binary Search

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

low = 0
high = len(L)-1
while(low<=high):
    mid = (low+high)//2
    if key == L[mid]:
        index = mid
        break
    elif key > L[mid]:
        low = mid+1
    else:
        high = mid-1

print(index)
