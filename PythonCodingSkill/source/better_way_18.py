def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log('My numbers are', [1, 2])
# log('Hi there')

favorites = [7, 33, 99]
log(1, 'Favorite colors', *favorites)
log('Favorite numbers', 7, 33)


# 문제1
## 가변 인수가 함수에 전달되기 앞서 항상 튜플로 변환된다는 점이다.
## 이는 함수를 호출하는 쪽에서 제너레이터에 * 연산자를 쓰면 제너레이터가 모두 소진될 까지 순회됨을 의미한다.
## 결과로 만들어지는 튜플은 제너레이터로부터 생성된 모든 값을 담으므로 메모리를 많이 차지해 결국 프로그램이
## 망가지게 된다.

def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

# 문제2
## 호출 코드를 모두 변경하지 않고서는 새 위치 인수를 추가할 수 없다는 점이다.
## 인수 리스트의 앞족에 위치 인수를 추가
## => 키워드 전용 인수를 사용해야 한다.