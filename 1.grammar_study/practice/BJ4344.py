
import sys
rinput = sys.stdin.readline

n1 = int(rinput())
for _ in range(n1):
    lstScore = list(map(int, rinput().split()))
    n2 = lstScore.pop(0)
    sum = 0
    count = 0
    for i in lstScore:
        sum += i
    for i in lstScore:
        if i > (sum / n2): count += 1
    
    print("{:.3f}%".format((count/n2) * 100))
