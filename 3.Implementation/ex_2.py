""" n = int(input())
cnt = 0

day = (n + 1) * 60 * 60 

for i in range(day):
    h = str(i // (60 * 60))
    i %= (60 * 60)
    m = str(i // 60)
    s = str(i % 60)

    if ('3' in h) or ('3' in m) or ('3' in s):
        cnt += 1

print(cnt) """


""" 
가능한 모든 시각의 경우를 하나씩 모두 세어서 푼다(완전 탐색)

 """

h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if 3 in str(i) + str(j) + str(k):
                count += 1

print(count)
