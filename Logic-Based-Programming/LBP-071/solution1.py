# Using Regular Expression

# Solution:

import re

def replaceVowel(s,ch):
    return (re.sub("[aeiou]",ch,s))

s=input()
print(replaceVowel(s,input()))
