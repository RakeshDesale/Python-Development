# Using max Function

# Solution:

def BlackJack(n1,n2):
    if n1>21 and n2>21:
        return 0
    elif n1==21 and n2==21:
        return 21
    elif n1>21:
        return n2
    elif n2>21:
        return n1
    else:
        return max(n1,n2)

n1=int(input())
n2=int(input())
print(BlackJack(n1,n2))
