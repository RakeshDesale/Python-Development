# Solution:

def nextLetter(s):
    nl=[]
    for i in s:
        nl.append(chr(ord(i)+1))
    return nl

print(''.join(nextLetter(input())))
