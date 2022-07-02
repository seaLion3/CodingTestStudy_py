import sys
rinput = sys.stdin.readline

n = int(rinput())
lstTime = list(map(int, rinput().split()))

lstTime.sort()

sumOfTime = 0
for i in range(n):
    for l in range(i+1):
        sumOfTime += lstTime[l]

print(sumOfTime)
