# Solution:

l=input().split()
print(l[-1],end=' ')
for i in range(len(l)-2,0,-1):
    print(l[i][::-1],end=' ')
print(l[0])
