# Another Approach Using Function

# Solution:

def arrsum(n):
    return sum([int(i) for i in n if i.endswith('3')])

n = int(input())
print(arrsum([i for i in input().split()]))
