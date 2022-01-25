# Solution:

str=input()
for i in str:
    if i>='A' and i<='Z':
        print(chr(ord(i)+32),end='')
    elif i>='a' and i<='z':
        print(chr(ord(i)-32),end='')
