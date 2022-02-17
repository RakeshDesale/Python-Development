# Without Using Function

# Solution:

s=input().lower()
for i in s:
    if i>='a' and i<='z':
        print(ord(i)-96,end=' ')
