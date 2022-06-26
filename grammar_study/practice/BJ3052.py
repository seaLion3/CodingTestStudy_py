
import imp


import sys
rinput = sys.stdin.readline

setN = set()
for _ in range(10):
    setN.add(int(input()) % 42)


print(len(setN))