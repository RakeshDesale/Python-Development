# Using Function

# Solution:

def modRes(b,e,m):
    return (b**e%m)

b,e,m = (int(i) for i in input().split())
print(modRes(b,e,m))
