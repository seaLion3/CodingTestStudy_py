
import imp


import sys
rinput = sys.stdin.readline

n = int(rinput())
lstScore = list(map(int, rinput().split()))

M = max(lstScore)
sum = 0

for i in lstScore:
    sum += (i/M)*100

print(sum / n)
