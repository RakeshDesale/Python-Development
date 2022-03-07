# Traditional (Reverse) Approach Using Function

# Solution:

def minElement(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] < L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L[n-1]

n = int(input())
print(minElement([int(i) for i in input().split()]))
