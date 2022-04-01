# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
count = 0
if n!=0:
    for i in L:
        if i>0:
            count+=1
        elif i==0:
            continue
        else:
            sum = sum + i
    print(count,sum)
else:
    print(" ")
