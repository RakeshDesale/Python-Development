# Using Core Logic and Using Function

# Solution:

def kShortExeTime(L,k):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    return L[k-1]

n = int(input())
k = int(input())
print(kShortExeTime([int(i) for i in input().split()],k))
