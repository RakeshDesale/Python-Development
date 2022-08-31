# Solution:

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for i in range(3):
    for j in range(3):
        temp = L[i][j]
        r = 0
        while temp != 0:
            d = temp % 10
            r = r * 10 + d
            temp = temp // 10
        print(r, end=' ')
    print()
