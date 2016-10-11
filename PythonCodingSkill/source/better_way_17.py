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

