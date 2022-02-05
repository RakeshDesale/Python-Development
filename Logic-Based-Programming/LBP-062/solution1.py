# Solution:

def findStr(str):
    return ("DUCK!" if "bomb" in str else "Relax, there's no bomb.")

print(findStr(input().lower()))
