# Traditional Approach

# Solution:

def replaceVowel(s,ch):
    newstr = ""
    for i in range(len(s)):
        if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            newstr = newstr + ch
        else:
            newstr = newstr + s[i]
    return newstr

s=input()
print(replaceVowel(s,input()))
