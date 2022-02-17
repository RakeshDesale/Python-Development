# Solution:

def alphabetPosition(s):
    for i in s:
        if i>='a' and i<='z':
            print(ord(i)-96,end=' ')

alphabetPosition(input().lower())
