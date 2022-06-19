# Using Function

# Solution:

def nearestWholeNumber(n):
    while(True):
        if n % 10 == 0:
            return n
        else:
            n += 1

print(nearestWholeNumber(int(input())))
