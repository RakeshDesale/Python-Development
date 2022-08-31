# Using Function

# Optimized Solution:

def isPrimeCount(L):
    count = 0
    for i in range(3):
        for j in range(3):
            for k in str(L[i][j]):
                if k in '2357':
                    count += 1
    return count

print(isPrimeCount([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]))
