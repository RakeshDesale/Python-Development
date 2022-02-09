# Without Using Function and Without Regular Expression

# Solution:

s=input()
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        continue
    else:
        print(s[i],end='')
