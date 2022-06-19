# Using Function

# Solution:

def rating(points):
    if points >= 30 and points <= 50:
        return "Average"
    elif points >= 51 and points <= 60:
        return "Good"
    elif points >= 61 and points <= 80:
        return "Excellent"
    else:
        return "Outstanding"

points = int(input())
if points >= 30 and points <= 100:
    print(rating(points))
else:
    pass
