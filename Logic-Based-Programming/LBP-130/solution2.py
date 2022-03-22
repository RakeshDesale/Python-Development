# Using Function

# Solution:

def nonRepeatElement(L,L2):
    for i in L:
        if i not in L2:
            L2.append(i)
    return L2

n = int(input())
L2=[]
L2 = nonRepeatElement([int(i) for i in input().split()],L2)
for i in L2:
    print(i,end=' ')
