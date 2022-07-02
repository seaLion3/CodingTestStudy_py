""" strData = input()

lstChr = []
lstInt = []

for i in strData:
    if '0' <= i <= '9':
        lstInt.append(int(i))
    else:
        lstChr.append(i)
lstChr.sort()
 """

data = input()
res = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        res.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
res.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    res.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변화하여 출력)
print(''.join(res))