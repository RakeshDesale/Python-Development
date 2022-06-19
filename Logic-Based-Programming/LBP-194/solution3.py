# Using Function

# Solution:

def updatePassword(i):
    if i >= 'A' and i <= 'Z':
        return (chr(ord(i) + 32))
    else:
        return (chr(ord(i) - 32))

st = input()
for i in range(len(st)):
    print(updatePassword(st[i]),end='')
