# Using Function

# Solution:

def sortedStr(s):
    for i in range(97,123):
        if chr(i) not in s:
            print(chr(i),end='')

sortedStr(input())