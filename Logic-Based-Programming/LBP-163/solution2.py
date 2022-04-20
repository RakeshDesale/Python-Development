# Another Approach

# Solution:

def uniqueNumber(L):
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and L[i] == L[j]:
                count += 1
        if count == 0:
            return L[i]

n = int(input())
print(uniqueNumber([int(i) for i in input().split()]))
