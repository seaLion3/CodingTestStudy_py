a, b = map(int, input().split())
c = int(input())

hour_c = (b + c) // 60 
min = (b + c) % 60
hour = 0

if 24 - a <= hour_c:
    hour = (a + hour_c) % 24
else:
    hour = a + hour_c


print(hour, min)

