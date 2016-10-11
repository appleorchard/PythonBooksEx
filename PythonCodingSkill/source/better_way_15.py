def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


# 파이썬은 클로저를 지원한다.
# 파이썬에서 함수는 일급 객체(first-class object)이다.
# 파이썬에는 튜플을 비교하는 특정한 규칙이 있다. 먼저 인덱스 0으로 아이템을 비교하고 그 다음으로 인덱스 1, 다음은 인덱스 2와 같이 진행한다.
## helper 클로저의 반환 값이 정렬 순서를 분리된 두 그룹으로 나뉘게 한 건 이 규칙 때문이다.

def sort_priority2(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print('Found: ', found)
print(numbers)


# 파이썬 인터프리터는 참조를 해결하려고 다음과 같은 순서로 스코프(scope)를 탐색한다.
# 1.현재의 함수 스코프
# 2.(현재 스코프를 담고 있는 다른 함수 같은) 감싸고 있는 스코프
# 3.코드를 포함하고 있는 모듈의 스코프(전역 스코프라고도 함)
# 4.(len이나 str 같은 함수를 담고 있는) 내장 스코프


# nonlocal을 사용할 때 복잡해지기 시작하면 헬퍼 클래스로 상태를 감싸는 방법을 이용한다.
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        else:
            return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True


# 파이썬 2의 스코프
def sort_priority(numbers, group):
    found = [False] # mutable

    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found[0]
