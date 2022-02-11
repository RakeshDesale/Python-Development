# Using Function

# Solution:

def removeDuplicate(s):
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    return l

print(''.join(removeDuplicate(input())))
