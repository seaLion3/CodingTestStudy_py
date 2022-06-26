
n = int(input())
cnt = 0
for i in range(1, n+1):
    lstNum = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif lstNum[0] - lstNum[1] == lstNum[1] - lstNum[2]:
        cnt += 1
         
print(cnt)



