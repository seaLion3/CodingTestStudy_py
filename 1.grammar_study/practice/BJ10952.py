import sys
rinput = sys.stdin.readline

while 1:
    a, b = map(int, rinput().split())
    if a==0 and b==0:
        break
    print(a+b)