# Using Function

# Solution:

def strEqual(L1,L2):
    L3 = []
    L4 = []
    for i in range(len(L1)-1):
        if L1[i] != '#' and L1[i+1] != '#':
            L3.append(L1[i])
    for i in range(len(L2)-1):
        if L2[i] != '#' and L2[i+1] != '#':
            L4.append(L2[i])
    return L3 == L4

L1 = input()
L2 = input()
print("1" if strEqual(L1,L2) else "0")
