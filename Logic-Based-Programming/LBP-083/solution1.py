# Solution:

import re
def firstNVowels(s,n):
    ns=re.sub("[^aeiouAEIOU]","",s)
    if n>len(ns):
        return "invalid"
    else:
        return ns[0:n]

s=input()
n=int(input())
print(firstNVowels(s,n))
