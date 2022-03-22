# Solution:

n = int(input())
L = [int(i) for i in input().split()]
d = {}
count = 0
for i in L:
    d[i] = d.get(i,0)+1
for i in d.values():
    if i>=2:
        count+=1
print(count)
