# Solution:

def longestWord(s):
    m=0
    st=""
    for i in s:
        if len(i)>m:
            m=len(i)
            st=i
    return st

print(longestWord(input().split()))
