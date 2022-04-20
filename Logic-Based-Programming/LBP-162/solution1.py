# Solution:

n = int(input())
L = [int(i) for i in input().split()]
count = 0
specialcount = 0
for i in L:
    x = str(i).count('5')
    if count <= x:
        count = x
        element = i
    if x == 0:
        specialcount += 1
print(element if specialcount !=n else L[0])
