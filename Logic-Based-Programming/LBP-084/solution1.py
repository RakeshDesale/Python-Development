# Solution:

def strOrder(s):
    l=list(s)
    l.sort()
    ns=''.join(l)
    return (s==ns)

print(str(strOrder(input())).lower())
