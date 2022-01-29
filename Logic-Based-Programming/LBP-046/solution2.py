# Solution:

day,month,year=[int(i) for i in input().split('-')]
if ((day*month==year%10) or (day*month==year%100) or(day*month==year%1000)):
    print("true")
else:
    print("false")
