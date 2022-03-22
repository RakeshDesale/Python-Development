# Another Approach Using Function

# Solution:

def nonRepeatElement(L):
    L2 = []
    for i in L:
        if i not in L2:
            L2.append(i)
    for i in L2:
        print(i,end=' ')

n = int(input())
nonRepeatElement([int(i) for i in input().split()])
