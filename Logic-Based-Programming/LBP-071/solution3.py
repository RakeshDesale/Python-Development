# Without Regular Expression Using List

# Solution:

def replaceVowel(s,ch):
    l=[]
    for i in s:
        if i in "aeiou":
            l.append(ch)
        else:
            l.append(i)
    return l

s=input()
print(''.join(replaceVowel(s,input())))
