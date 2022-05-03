# Using Function

# Solution:

def secretInfo(st):
    for i in st:
        if i.isupper() or i.isdigit():
            print(i,end='')

secretInfo(input())
