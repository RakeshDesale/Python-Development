# Using Traditional Approach

# Solution:

def validHex(s):
    count=0
    for i in range(len(s)):
        if(s[i]>='a' and s[i]<='z'):
            s[i]=s[i]-32
    
    if(s[0]=="#" and len(s)==7):
        for i in range(1,len(s)):
            if ((s[i]>='A' and s[i]<='F') or (s[i]>='0' and s[i]<='9')):
                count+=1
    return count==6

print(str(validHex(input())).lower())
