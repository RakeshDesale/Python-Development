# Another Approach Using Function

# Solution:

def secretInfo(st):
    for i in st:
        if ((i>='A' and i<='Z') or (i>='0' and i<='9')):
            print(i,end='')

secretInfo(input())
