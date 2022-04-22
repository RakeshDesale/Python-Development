# Solution:

n = int(input())
L = [int(i) for i in input().split()]
print("true" if L == L[::-1] else "false")
