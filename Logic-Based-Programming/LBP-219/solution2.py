# Using Function

# Solution:

def oddEvenFreq(L):
    oddcount = 0
    evencount = 0
    for i in range(3):
        for j in range(3):
            if L[i][j] % 2 == 0 and L[i][j] != 0:
                evencount += 1
            elif L[i][j] % 2 != 0 and L[i][j] != 0:
                oddcount += 1
    print(oddcount)
    print(evencount)

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
oddEvenFreq(L)
