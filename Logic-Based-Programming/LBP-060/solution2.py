# Using Function

# Solution:

from collections import Counter
def maxChar(str):
    maxchar=Counter(str)
    return(max(maxchar,key=maxchar.get))

print(maxChar(input()))
