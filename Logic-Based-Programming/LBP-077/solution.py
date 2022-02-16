# Solution:

from itertools import permutations
l=list(permutations(input()))
for i in l:
    print(''.join(i),end=' ')
