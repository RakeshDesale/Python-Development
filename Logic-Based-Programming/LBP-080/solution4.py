# Using Traditional Approach and Without Using Function

# Solution:

s=input()
count=0
for i in range(0,len(s)):
    if s[i]>='a' and s[i]<='z':
        s[i]=s[i]-32

if s[0]=='#' and len(s)==7:
    for i in range(1,len(s)):
        if ((s[i]>='A' and s[i]<='F') or (s[i]>='0' and s[i]<='9')):
            count+=1
        
print("true" if count==6 else "false")
