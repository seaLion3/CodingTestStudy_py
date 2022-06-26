
import sys
rinput = sys.stdin.readline

n = int(rinput())

for _ in range(n):
    sum = 0
    score = 0
    strOX = rinput().rstrip()
    for i in (strOX):
        if i == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)

            
            
        