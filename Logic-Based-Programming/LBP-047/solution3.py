# Without Using Function in One Line

# Solution:

print("Evenish" if sum([int(i) for i in input()])%2==0 else "Oddish")
