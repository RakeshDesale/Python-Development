# Using Function, ASCII and Using Constraints

# Solution:

def isChessBoard(str):
    if len(str)==2:
        if ((ord(str[0])>=97 and ord(str[0])<=104) and (ord(str[1])>=49 and ord(str[1])<=56)):
            x=ord(str[0])-96
            y=ord(str[1])
            return (x%2!=y%2)
        else:
            pass
    else:
        pass

print(str(isChessBoard(input())).lower())
