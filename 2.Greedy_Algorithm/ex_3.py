""" def add(a, b):
    return a + b

def mul(a, b):
    return a * b

lstStr = list(input())
res = 0
a = int(lstStr[0])

for i in range(len(lstStr)-1):
    b = int(lstStr[i+1])
    if add(a, b) > mul(a, b):
        res = add(a, b)
    else:
        res = mul(a, b)
    a = res
print(res) """


from unittest import result


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱보다는 더하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

