# Solution:

st = input()
n = int(input())
L = [int(i) for i in input().split()]
for i in range(len(st)):
    for j in L:
        if j == i:
            print(st[i].lower(),end='')
