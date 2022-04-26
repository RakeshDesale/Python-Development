# Using Function

# Solution:

def prodBarcode(i):
    return ord(i)-97

st = input()
for i in st:
    print(prodBarcode(i),end='')
