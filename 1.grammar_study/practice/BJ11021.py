import sys
rinput = sys.stdin.readline

n = int(rinput())
for i in range(n):
    a, b = map(int, rinput().split())
    print(f"Case #{i+1}: {a+b}")
