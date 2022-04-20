# Without Using Function

# Solution:

n1 = int(input())
L1 = [int(i) for i in input().split()]
n2 = int(input())
L2 = [int(i) for i in input().split()]
L3 = L1 + L2
L3.sort()
counter = 0
for i in range(0,(n1+n2)-1):
    if(L3[i]+1==L3[i+1]):
        counter += 1
print(str(counter==(n1+n2)-1).lower())
