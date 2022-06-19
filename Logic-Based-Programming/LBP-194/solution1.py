# Solution:

st = input()
for i in range(len(st)):
    if st[i] >= 'A' and st[i] <= 'Z':
        print(chr(ord(st[i]) + 32),end='')
    else:
        print(chr(ord(st[i]) - 32),end='')
