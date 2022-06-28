n = 1260
count = 0

lst = [500, 100, 50, 10]

for coin in lst:
    count += n // coin
    n %= coin

print(count)