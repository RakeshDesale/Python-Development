# Solution:

def minToSec(L):
    if L[0]=='0':
        min=convert(L[1])
    else:
        min=convert(L[0])*10+convert(L[1])
    if L[3]=='0':
        sec=convert(L[4])
    else:
        sec=convert(L[3])*10+convert(L[4])
    return min*60+sec

def convert(s):
    return ord(s)-48

L=[i for i in input()]
print(minToSec(L))
