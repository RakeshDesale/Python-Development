# Using Function Without Regular Expression

# Solution:

def removeVowel(s):
    s1=[]
    for i in range(0,len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            continue
        else:
            s1.append(s[i])
    return s1

print(''.join(removeVowel(input())))
