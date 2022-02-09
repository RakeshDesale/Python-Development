# Using Function and Constraints

# Solution:

def isChessBoard(str):
    if len(str)==2:
        if ((str[0]>='a' and str[0]<='h') and (str[1]>='1' and str[1]<='8')):
            x=ord(str[0])-96
            y=ord(str[1])
            return (x%2!=y%2)
        else:
            pass
    else:
        pass

print(str(isChessBoard(input())).lower())
