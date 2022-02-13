# Using Function

# Solution:

def evenLengthWord(s):
    s=[i for i in s if len(i)%2==0]
    return s

print(' '.join(evenLengthWord(input().split())))
