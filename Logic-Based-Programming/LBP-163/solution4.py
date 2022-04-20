# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    count = 0
    for j in range(n):
        if i != j and L[i] == L[j]:
            count += 1
    if count == 0:
        print(L[i])
