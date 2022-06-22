# Solution:

L1 = input()
L2 = input()
L3 = []
L4 = []
for i in range(len(L1)-1):
    if L1[i] != '#' and L1[i+1] != '#':
        L3.append(L1[i])
for i in range(len(L2)-1):
    if L2[i] != '#' and L2[i+1] != '#':
        L4.append(L2[i])
print("1" if L3 == L4 else "0")
