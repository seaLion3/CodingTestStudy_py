
from itertools import count


n = 1
for _ in range(3):
    n = n * int(input())

n = str(n) 
for i in range(10):
    print(n.count(str(i)))

