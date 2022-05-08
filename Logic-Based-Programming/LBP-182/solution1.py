# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
L1 = []
for i in L:
    factors = 0
    for j in range(1,i+1):
        if i%j == 0:
            factors += 1
    if factors == 2:
        L1.append(i)
L1.sort()
if len(L1)>=2:
    print(abs(L1[len(L1)-1] - L1[0]))
else:
    print(0)
