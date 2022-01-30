# Without Using Function

# Solution:

L=[ord(i) for i in input()]
if L[0]=='0':
    min=L[1]-48
else:
    min=(L[0]-48)*10+L[1]-48
if L[3]=='0':
    sec=L[4]-48
else:
    sec=(L[3]-48)*10+L[4]-48
print(min*60+sec)
