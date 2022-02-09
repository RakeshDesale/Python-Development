# Using Function and Regular Expression

# Solution:

import re

def removeVowel(s):
    return (re.sub("[aeiou]","",s))

print(removeVowel(input()))
