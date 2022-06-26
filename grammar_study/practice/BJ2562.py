import sys
rinput = sys.stdin.readline
lstN = []

for _ in range(9):
    lstN.append(int(rinput()))

print(max(lstN))
print(lstN.index(max(lstN))+1)