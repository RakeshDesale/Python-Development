# Using Tuple and Using Function

# Solution:

def scoreBoard(s):
    return(s.count('A'),s.count('B'),s.count('C'))

t=(scoreBoard(input()))
for i in t:
    print(i,end=' ')
