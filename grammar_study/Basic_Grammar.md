
# 리스트 자료형

## 리스트 컴프리헨션

```python
array1 = [i for i in range(10)]
print(array1)

array2 = [i for i in range(20) if i % 2 == 1]   
print(array2)

array3 = [i*i for i in range(1, 10)]
print(array3)

# 리스트 컴프리헨션 2차원 리스트
m=3
n=4
array4 = [[0] * m for _ in range(n)]        
print(array4)
# [[0] * m] * n 잘못된 예시 전체 리스트 안에 포홤된 각 리스트가 모두 같은 객체로 인식 
```
## 리스트 매서드
```python
"""
append()
sort(), sort(reverse=True)
insert()
count()
remove()
"""

# 리스트에서 특정 값을 가지는 원소를 모두 제거

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
```

<br/><br/><br/>
# 튜플 자료형

튜플을 사용하면 좋은 경우

* 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
    * 최단 경로 알고리즘에서 (비용, 노드 번호)의 형태로 자료형을 자주 사용
* 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
    * 튜플은 변경이 불가능함으로 리스트와 다르게 키 값으로 사용 가능
* 리스트보다 메로리 효율적으로 사용해야 할 때

<br/><br/><br/>
# 사전 자료형

```python
data = dict() 
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
print(data.keys())
print(data.values())

b = {
    '홍길동' : 97,
    '이순신' : 98
}
print(b)
```

<br/><br/><br/>
# 집합 자료형
어떤 데이터의 존재여부 확인할때 사용한다
```python
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)
```

집합 자료형의 연산  
합집함 : |  
교집합 : &  
차집합 : -  
add()  
update()  
remove()  

<br/><br/><br/>

# 기본 입출력


>input() 함수는 한 줄의 문자열을 입력 받는 함수이다  
map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용  

```python
list(map(int, input().split()))
a, b, c = map(int, input().split())

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
```

## 빠르게 입력 받기

* 사용자로 부터 입력을 최대한 빠르게 받아야 하는경우  
  * 파이썬의 경우 sys라이브러리에 정의 되어있는 sys.stdin.readline() 메서드를 사용  
  * 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력 되므로 rstrip() 메서를 함꼐 사용
이진탐색, 정렬, 그래프 문제에서 주로 사용

```python
import sys
# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)
```

```python
# f-string
answer = 7 
print(f"정답은 {answer}입니다.")
```

<br/><br/><br/>
# 조건문

## 아무것도 처리하고 싶지 않을 때 pass 키워드 사용

```python
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')
print('프로그램을 종료합니다.')
```

<br/>

## 조건문의 간소화
```python
score = 85

if score >= 80: result = 'Success'
else: result = 'Fail'

score = 85
result = 'Success' if score >= 80 else 'Fail'

print(result)
```

<br/>

## 수학의 부등식을 그대로 사용가능하다
```python
x = 15
if 0 < x < 20:
    print("True")
```

<br/><br/><br/>
# 반복문 

>while보다는 for추천
반복문 작성한 뒤에는 항상 반복문을 탈출할 수 있는지를 확인한다.

<br/><br/><br/>
# 함수 
## 파이썬에서는 여러 개의 반환 값을 가질 수 있다.(패킹)
```python
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)
```

<br/><br/><br/>

# 람다 표현식 
>한번만 사용하는 함수에서 사용

<br/>

```python
print((lambda a, b: a + b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))
```

<br/>

```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))
```

<br/><br/><br/>
# 유용한 표준 라이브러리

* 내장함수 
* itertools   반복되는 형태의 데이터 처리(순열과 조합 라이브러리 : 완전 탐색 유형)
* heapq : 힙(Heap), 우선순위 큐 
* bisect : 이진 탐색
* collections : 덱(deque), 카운터(Counter)
* math 

<br/>

## 내장 함수

<br/>

```python
result = sum([1, 2, 3, 4, 5])
print(result)

min_result = min(7, 3, 5, 2)
max_result = max([7, 3, 5, 2])
print(min_result, max_result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key = lambda x: x[1], reverse=True)
print(result)
```

<br/>

## 순열과 조합

<br/>

```python
from itertools import permutations

from sympy import re
data = ['A', 'B', 'C'] 
result = list(permutations(data, 3))
print(result)

from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복 순열과 중복 조합

from itertools import product
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

from itertools import combinations_with_replacement
data = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
```

## Counter

<br/>

```python
from collections import Counter
counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 반환
```