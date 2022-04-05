# Another Approach Using Function

# Solution:

def lowest2Sum(L):
    L=sorted(L)
    sum = 0
    for i in range(len(L)):
        if L[i]>0:
            sum = L[i] + L[i+1]
            break
    return sum

n = int(input())
print(lowest2Sum([int(i) for i in input().split()]))
