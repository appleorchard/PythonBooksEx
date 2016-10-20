# collections 모듈의 deque 클래스는 더블 앤드 큐(double-ended queue)다.
# deque은 큐의 처음과 끝에서 아이템을 삽입하거나 삭제할 때 항상 일정한 시간이 걸리는 연산을 제공한다.
from bisect import bisect_left
from collections import deque, OrderedDict, defaultdict

fifo = deque()
fifo.append(1)  # 생산자
x = fifo.popleft()  # 소비자

# 리스트의 시작 부분에서 아이쳄을 삽입하거나 삭제하는 연산에는 선형적 시간(linear time)이 걸리므로 deque의 일정한 시간보다 훨씬 느리다.

from random import randint

a = {}
a['foo'] = 1
a['bar'] = 2

while True:
    z = randint(99, 1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['foo'] = 1
    b['bar'] = 2
    for i in range(z):
        del b[i]
    if str(b) != str(a):
        break

print(a)
print(b)
print('Equal?', a == b)

# collections 모듈의 OrderedDict 클래스는 키가 삽입된 순서를 유지하는 특별한 딕셔너리 타입이다.
# OrderedDict의 키를 순회하는 것은 예상 가능한 동작이다.
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2

b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for value1, value2 in zip(a.values(), b.values()):
    print(value1, value2)

# 딕셔너리는 통계를 관리하고 추적하는 작업에 유용하다. 딕셔너리를 사용할 때 한 가지 문제는 어떤 키가 이미 존재한다고 가정할 수 없다는 점이다.
# 이 문제 때문에 딕셔너리에 저장된 카운터를 증가시키는 것처럼 간단한 작업도 까다로워진다.
# stats = {}
key = 'my_counter'
# if key not in stats:
#     stats[key] = 0
# stats[key] += 1

stats = defaultdict(int)
stats['my_counter'] += 1

print(stats)

from heapq import heappush, heappop, nsmallest
# 힙 큐
# 힙(heap)은 우선순위 큐(priority queue)를 유지하는 유용한 자료 구조다.
# headq 모듈은 표준 list 타입으로 힙을 생성하는 heappush, heappop, nsmallest 같은 함수를 제공한다.
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

# 아이템은 가장 우선순위가 높은 것(가장 낮은 수)부터 제거된다.
# print(heappop(a), heappop(a), heappop(a), heappop(a))
assert a[0] == nsmallest(1, a)[0] == 3
print('Before:', a)
a.sort()
print('After:', a)

# 바이섹션
# list에서 아이템을 검색하는 작업은 index 메서드를 호출할 때 리스트의 길이에 비례한 선형적 시간이 걸린다.
from time import time

start = time()
x = list(range(10 ** 6))
# i = x.index(991234)
i = bisect_left(x, 991234)
print(i)

end = time()
print('time: %f' % (end - start))

# 이터레이터 도구

