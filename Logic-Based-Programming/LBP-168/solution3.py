# Using Function

# Solution:

def arrPali(L):
    return L == L[::-1]

n = int(input())
L = [int(i) for i in input().split()]
print("true" if arrPali(L) else "false")
