# Traditional Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in range(0,len(L)):
    temp = L[i]
    rev = 0
    while L[i]!=0:
        d = L[i]%10
        rev = rev*10+d
        L[i] = L[i]//10
    if temp == rev:
        sum = sum + temp
print(sum,end=' ')
