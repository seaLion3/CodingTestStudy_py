
""" N, K = map(int,input().split())
cnt = 0

while N != 1:
    if N % K == 0:
        N /= K

    else:
        N -= 1
    cnt += 1

print(cnt) """


"""
최대한 많이 나누기 수행
-> 2이상의 수로 나누는 작업이 1을 뺴는 작업보다 효율적
"""

n, k = map(int, input().split())

result = 0
 
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 뺴기
    target = (n // k ) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k 

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

