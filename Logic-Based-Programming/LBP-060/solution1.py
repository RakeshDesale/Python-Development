# Solution:

from collections import Counter
maxchar=Counter(input())
print(max(maxchar,key=maxchar.get))
