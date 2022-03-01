# Traditional Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in L:
    if i%10==3:
        sum = sum+i
print(sum)
