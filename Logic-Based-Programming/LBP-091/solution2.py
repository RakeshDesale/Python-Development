# Solution:

def alphabetPosition(s):
    for i in range(len(s)):
        if s[i]>='a' and s[i]<='z':
            print(ord(s[i])-96,end=' ')

alphabetPosition(input().lower())
