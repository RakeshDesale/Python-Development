# Solution:

points = int(input())
if points >= 30 and points <= 100:
    if points >= 30 and points <= 50:
        print("Average")
    elif points >= 51 and points <= 60:
        print("Good")
    elif points >= 61 and points <= 80:
        print("Excellent")
    else:
        print("Outstanding")
else:
    pass
