# Using Function

# Solution:

def isChessBoard(str):
    x=ord(str[0])-96
    y=ord(str[1])
    return (x%2!=y%2)

print(str(isChessBoard(input())).lower())
