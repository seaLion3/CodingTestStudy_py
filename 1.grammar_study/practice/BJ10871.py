import sys
rinput = sys.stdin.readline

N, X = map(int, rinput().split())
lstInt = list(map(int, rinput().split()))
lstNew = []

for i in lstInt:
    if i < X:
        print(i, end=" ")



