# Solution:

str=input()
a=[int (i) for i in input().split()]
ts=[0]*len(str)
for i in range(0,len(str)):
    ts[a[i]]=str[i]
print(''.join(ts))
