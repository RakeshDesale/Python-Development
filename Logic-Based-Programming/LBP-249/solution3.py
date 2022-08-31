# Using Function

# Solution:

def rev(n):
    r = 0
    while n != 0:
        d = n % 10
        r = r * 10 + d
        n = n // 10
    return r

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for i in range(3):
    for j in range(3):
        print(rev(L[i][j]), end=' ')
    print()
