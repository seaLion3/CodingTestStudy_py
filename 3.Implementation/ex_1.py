# n = int(input())
# lstDirection = list(input().split())
# x = y = 1

# for i in lstDirection:
#     a = x
#     b = y

#     if i == 'L':
#         b -= 1
#     elif i == 'R':
#         b += 1
#     elif i == 'U':
#         a -= 1
#     elif i == 'D':
#         a += 1
    
#     if (1 <= a <= n) and (1 <= b <= n):
#         x = a
#         y = b

# print(x, y)

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)