# Solution:

def replaceVowel(s,ch):
    newstr=""
    for i in s:
        if i in "aeiou":
            newstr = newstr + ch
        else:
            newstr = newstr + i
    return newstr

s=input()
print(replaceVowel(s,input()))
