# Using Function and Using Core Logic

# Solution:

def lowest2Sum(L):
    sum = 0
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    for i in range(len(L)):
        if L[i]>0:
            sum = L[i] + L[i+1]
            break
    return sum

n = int(input())
print(lowest2Sum([int(i) for i in input().split()]))
