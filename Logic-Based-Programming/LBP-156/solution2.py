# Optimized Solution:

st = input()
n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    print(st[L[i]].lower(),end='')
