# Using Function

# Solution:

def luckyNumber(L):
    count = 0
    specialcount = 0
    for i in L:
        x = str(i).count('5')
        if count <= x:
            count = x
            element = i
        if x == 0:
            specialcount += 1
    return element if specialcount !=n else L[0]

n = int(input())
L = [int(i) for i in input().split()]
print(luckyNumber(L))
