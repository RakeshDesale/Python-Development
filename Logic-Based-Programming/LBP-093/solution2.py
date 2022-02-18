# Using Function

# Solution:

def nonRepeatChar(s):
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    
nonRepeatChar(input())
