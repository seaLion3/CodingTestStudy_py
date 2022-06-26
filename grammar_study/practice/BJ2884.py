hour, min = map(int, input().split())

if min >= 45:
    min -= 45
else:
    min = 60 + (min - 45)
    if hour == 0:
        hour = 23
    else:
        hour -= 1

print(hour, min)