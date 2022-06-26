
# ����Ʈ �ڷ���

## ����Ʈ ���������

```python
array1 = [i for i in range(10)]
print(array1)

array2 = [i for i in range(20) if i % 2 == 1]   
print(array2)

array3 = [i*i for i in range(1, 10)]
print(array3)

# ����Ʈ ��������� 2���� ����Ʈ
m=3
n=4
array4 = [[0] * m for _ in range(n)]        
print(array4)
# [[0] * m] * n �߸��� ���� ��ü ����Ʈ �ȿ� ���c�� �� ����Ʈ�� ��� ���� ��ü�� �ν� 
```
## ����Ʈ �ż���
```python
"""
append()
sort(), sort(reverse=True)
insert()
count()
remove()
"""

# ����Ʈ���� Ư�� ���� ������ ���Ҹ� ��� ����

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # ���� �ڷ���

# remove_list�� ���Ե��� ���� ������ ����
result = [i for i in a if i not in remove_set]
print(result)
```

<br/><br/><br/>
# Ʃ�� �ڷ���

Ʃ���� ����ϸ� ���� ���

* ���� �ٸ� ������ �����͸� ��� �����ؾ� �� ��
    * �ִ� ��� �˰��򿡼� (���, ��� ��ȣ)�� ���·� �ڷ����� ���� ���
* �������� ������ �ؽ�(Hashing)�� Ű ������ ����ؾ� �� ��
    * Ʃ���� ������ �Ұ��������� ����Ʈ�� �ٸ��� Ű ������ ��� ����
* ����Ʈ���� �޷θ� ȿ�������� ����ؾ� �� ��

<br/><br/><br/>
# ���� �ڷ���

```python
data = dict() 
data['���'] = 'Apple'
data['�ٳ���'] = 'Banana'
data['���ڳ�'] = 'Coconut'

print(data)
print(data.keys())
print(data.values())

b = {
    'ȫ�浿' : 97,
    '�̼���' : 98
}
print(b)
```

<br/><br/><br/>
# ���� �ڷ���
� �������� ���翩�� Ȯ���Ҷ� ����Ѵ�
```python
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)
```

���� �ڷ����� ����  
������ : |  
������ : &  
������ : -  
add()  
update()  
remove()  

<br/><br/><br/>

# �⺻ �����


>input() �Լ��� �� ���� ���ڿ��� �Է� �޴� �Լ��̴�  
map() �Լ��� ����Ʈ�� ��� ���ҿ� ���� Ư���� �Լ��� ������ �� ���  

```python
list(map(int, input().split()))
a, b, c = map(int, input().split())

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
```

## ������ �Է� �ޱ�

* ����ڷ� ���� �Է��� �ִ��� ������ �޾ƾ� �ϴ°��  
  * ���̽��� ��� sys���̺귯���� ���� �Ǿ��ִ� sys.stdin.readline() �޼��带 ���  
  * �Է� �� ����(Enter)�� �� �ٲ� ��ȣ�� �Է� �ǹǷ� rstrip() �޼��� �Բ� ���
����Ž��, ����, �׷��� �������� �ַ� ���

```python
import sys
# ���ڿ� �Է� �ޱ�
data = sys.stdin.readline().rstrip()
print(data)
```

```python
# f-string
answer = 7 
print(f"������ {answer}�Դϴ�.")
```

<br/><br/><br/>
# ���ǹ�

## �ƹ��͵� ó���ϰ� ���� ���� �� pass Ű���� ���

```python
score = 85

if score >= 80:
    pass # ���߿� �ۼ��� �ҽ��ڵ�
else:
    print('������ 80�� �̸��Դϴ�.')
print('���α׷��� �����մϴ�.')
```

<br/>

## ���ǹ��� ����ȭ
```python
score = 85

if score >= 80: result = 'Success'
else: result = 'Fail'

score = 85
result = 'Success' if score >= 80 else 'Fail'

print(result)
```

<br/>

## ������ �ε���� �״�� ��밡���ϴ�
```python
x = 15
if 0 < x < 20:
    print("True")
```

<br/><br/><br/>
# �ݺ��� 

>while���ٴ� for��õ
�ݺ��� �ۼ��� �ڿ��� �׻� �ݺ����� Ż���� �� �ִ����� Ȯ���Ѵ�.

<br/><br/><br/>
# �Լ� 
## ���̽㿡���� ���� ���� ��ȯ ���� ���� �� �ִ�.(��ŷ)
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

# ���� ǥ���� 
>�ѹ��� ����ϴ� �Լ����� ���

<br/>

```python
print((lambda a, b: a + b)(3, 7))

array = [('ȫ�浿', 50), ('�̼���', 32), ('�ƹ���', 74)]

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
# ������ ǥ�� ���̺귯��

* �����Լ� 
* itertools   �ݺ��Ǵ� ������ ������ ó��(������ ���� ���̺귯�� : ���� Ž�� ����)
* heapq : ��(Heap), �켱���� ť 
* bisect : ���� Ž��
* collections : ��(deque), ī����(Counter)
* math 

<br/>

## ���� �Լ�

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

array = [('ȫ�浿', 35), ('�̼���', 75), ('�ƹ���', 50)]
result = sorted(array, key = lambda x: x[1], reverse=True)
print(result)
```

<br/>

## ������ ����

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

# �ߺ� ������ �ߺ� ����

from itertools import product
result = list(product(data, repeat=2)) # 2���� �̴� ��� ���� ���ϱ� (�ߺ� ���)
print(result)

from itertools import combinations_with_replacement
data = list(combinations_with_replacement(data, 2)) # 2���� �̴� ��� ���� ���ϱ� (�ߺ� ���)
print(result)
```

## Counter

<br/>

```python
from collections import Counter
counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter)) # ���� �ڷ������� ��ȯ
```