# Without Using Function

# Solution:

s=input().lower()
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        print(ord(s[i])-96,end=' ')
