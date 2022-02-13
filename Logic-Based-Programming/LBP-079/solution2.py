# Using Function

# Solution:

def swapWords(s):
    print(s[-1],end=' ')
    for i in range(len(s)-2,0,-1):
        print(s[i][::-1],end=' ')
    print(s[0])
    
swapWords(input().split())
