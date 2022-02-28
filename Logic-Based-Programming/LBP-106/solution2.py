# Another Approach

# Solution:

n = int(input())
L = [i for i in input().split()]
sum=0;
for i in L:
    if i == i[::-1]:
        sum = sum + int(i)
print(sum)
