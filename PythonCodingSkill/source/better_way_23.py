names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)


# 다른 언어에서라면 후크를 추상 클래스로 정의할 것이라고 예상할 수도 있다.
# 파이썬의 후크 중 상당수는 인수와 반환 값을 잘 정의해놓은 단순히 상태가 없는 함수이다.
# 파이썬의 함수는 일급 함수이기 때문에 후크로 사용될 수 있다.

def log_missing():
    print('key added')
    return 0


from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # 상태 보존 클로저
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


result, count = increment_with_report(current, increments)
assert count == 2


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
# counter()
# assert callable(counter)

result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2



