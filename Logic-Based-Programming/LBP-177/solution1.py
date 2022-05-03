# Solution:

st = input()
for i in st:
    if i.isupper() or i.isdigit():
        print(i,end='')
