# Using Core Logic

# Solution:

def conSeq(L1,L2,n1,n2):
    L3 = L1 + L2
    for i in range(0,(n1+n2)):
        for j in range(i+1,(n1+n2)):
            if L3[i]>L3[j]:
                L3[i],L3[j] = L3[j],L3[i]
    counter = 0
    for i in range(0,(n1+n2)-1):
        if(L3[i]+1==L3[i+1]):
            counter += 1
    return (counter==(n1+n2)-1)


n1 = int(input())
L1 = [int(i) for i in input().split()]
n2 = int(input())
L2 = [int(i) for i in input().split()]
print(str(conSeq(L1,L2,n1,n2)).lower())
