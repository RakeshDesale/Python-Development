# Without Using Function

# Solution:

import re
s=input()
n=int(input())
ns=re.sub("[^aeiouAEIOU]","",s)
print("invalid" if n>len(ns) else ns[0:n])
