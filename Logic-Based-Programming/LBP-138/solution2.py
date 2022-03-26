# Using Function

# Solution:

def countEvenOdd(L):
    countEven = 0
    countOdd = 0
    for i in L:
        if i%2==0:
            countEven+=1
        else:
            countOdd+=1
    return countEven,countOdd

n = int(input())
L = countEvenOdd([int(i) for i in input().split()])
for i in L:
    print(i)
