# Using String replace() Method

# Solution:

def replaceVowel(st,ch):
    for i in "aeiou":
        st=st.replace(i,ch)
    return st

s=input()
print(replaceVowel(s,input()))
