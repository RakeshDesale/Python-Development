# Another Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
count=0
key = int(input())
for i in L:
    if i==key:
        count+=1
print(count)
