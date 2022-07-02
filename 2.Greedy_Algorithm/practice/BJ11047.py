n, k = map(int, input().split())
lstCoin = []
for _ in range(n):
    c = int(input())
    lstCoin.append(c)

lstCoin.sort(reverse=True)

cnt = 0
for i in lstCoin:
    cnt += k // i
    k %= i
    if k == 0:
        break

print(cnt)

    
 