import sys
rinput = sys.stdin.readline

n = int(rinput())
for _ in range(n):
    a, b = rinput().rsplit()
    for i in list(b):
        print(i*int(a), end="")
    print()

