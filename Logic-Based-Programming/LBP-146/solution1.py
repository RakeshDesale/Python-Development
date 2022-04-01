# Solution:

def countSum(L):
    sum = 0
    count = 0
    for i in L:
        if i>0:
            count+=1
        elif i==0:
            continue
        else:
            sum = sum + i
    print(count,sum)

n = int(input())
L = [int(i) for i in input().split()]
if n!=0:
    countSum(L)
else:
    print(" ")
