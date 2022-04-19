# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
count = 0
for i in range(n-1):
    for j in str(L[i]):
        if j in str(L[i+1]):
            count += 1
            break
print(str(count==n-1).lower())
