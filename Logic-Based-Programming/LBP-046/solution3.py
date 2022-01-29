# Optimized Solution:

day,month,year=[int(i) for i in input().split('-')]
print("true" if((day*month==year%10) or (day*month==year%100) or(day*month==year%1000)) else "false")
