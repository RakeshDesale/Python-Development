# Another Approach

# Solution:

n = int(input())
print(sum([int(i) for i in input().split() if i.endswith('3')]))
