def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 이미 소진한 이터레이터를 순회하더라도 오류가 일어나지 안는다.
def normalize_copy(numbers):
    numbers = list(numbers)  # 리스트에 대한 복사본을 생성
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 복사본이 클 경우 문제다. 이터레이터를 복사하면 프로그램의 메모리가 고갈되어 동작을 멈출 수 있다.
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


visits = ReadVisits('tmp/my_file.txt')
percentages = normalize_defensive(visits)
print(percentages)

it = read_visits('tmp/my_file.txt')
percentages = normalize_defensive(it)

# 입력 인수를 여러번 순회하는 함수를 작성할 때 주의하자. 입력 인수가 이터레이터라면 이상하게 동작해서 값을 잃어버릴 수 있다.