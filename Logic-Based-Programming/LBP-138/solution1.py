# Solution:

n = int(input())
L = [int(i) for i in input().split()]
countEven = 0
countOdd = 0
for i in L:
    if(i%2==0):
        countEven+=1
    else:
        countOdd+=1
print(countEven)
print(countOdd)
