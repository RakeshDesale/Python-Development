# Using Function

# Solution:

def isPrimeCount(L):
    count2 = 0
    for i in range(3):
        for j in range(3):
            count1 = 0
            while L[i][j] != 0:
                d = L[i][j] % 10
                if d == 2 or d == 3 or d == 5 or d == 7:
                    count1 += 1
                L[i][j] = L[i][j] // 10
            count2 = count2 + count1
    return count2

print(isPrimeCount([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]))
