# Using Function

# Solution:

def sumDiff(n):
    L = []
    while n!=0:
        L.append(n%10)
        n = n//10
    index = 0
    sumEven = 0
    sumOdd = 0
    while index < len(L):
        if index%2 == 0:
            sumEven = sumEven + L[index]
        else:
            sumOdd = sumOdd + L[index]
        index += 1
    return (sumOdd - sumEven)

n = input()
n = int(n[::-1])
print(sumDiff(n))
