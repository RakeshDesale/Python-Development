# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
count = 0
for i in L:
    factors = 0
    for j in range(1,i+1):
        if i%j==0:
            factors += 1
    if factors==2:
        count += 1
print("true" if count==n else "false")
