# Solution:

n = int(input())
l = [int(i) for i in input().split()]
sum=0
for i in l:
    factors=0
    for j in range(1,i+1):
        if i%j==0:
            factors+=1
    if factors==2:
        sum = sum + i
print(sum)
