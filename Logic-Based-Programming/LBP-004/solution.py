# Solution:

salecount=int(input())
if salecount>=30 and salecount<=100:
    if salecount>=30 and salecount<=50:
        print("D")
    elif salecount>=51 and salecount<=60:
        print("C")
    elif salecount>=61 and salecount<=80:
        print("B")
    else:
        print("A")
else:
    print("invalid")
