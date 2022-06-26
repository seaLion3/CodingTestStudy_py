import sys
rinput = sys.stdin.readline

while 1:
    try:
        a, b = map(int, rinput().split())
        print(a+b)
    except:
        break