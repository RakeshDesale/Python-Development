# Using Function

# Solution:

def findWord(L,st):
    return ("true" if st in L else "false")

L = ["break","case","continue","default","defer","else","for","func","goto","if","map","range","return","struct","type","var"]
st = input()
print(findWord(L,st))
