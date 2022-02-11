# Without Using Function

# Solution:

l=input().split()
m=0
s=""
for i in l:
    if len(i)>m:
        m=len(i)
        s=i
print(s)
