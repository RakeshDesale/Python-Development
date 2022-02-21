# Solution:

def firstLetterOfWord(s):
    for i in s:
        print(i[0],end='')
    
firstLetterOfWord(input().split())
