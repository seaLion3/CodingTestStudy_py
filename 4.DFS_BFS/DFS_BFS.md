# DFS / BFS

## 1. 설명
* 탐색(Search) 
  * 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
* 대표적 그래프 탐색 알고리즘
  * DFS / BFS

</br>

## 2. Stack

* 선입후출, 입구와 출구가 동일
* 파이썬에서는 list자료형 이용(append, pop)
  
## 3. queue

* 선입선출, 입구와 출구가 분리, 대기열
* 파이썬에서는 deque라이브러리 사용

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```
