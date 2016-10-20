# 파이선 표준 구현 CPython
# 1. 소스 텍스트를 바이트코드(bytecode)로 파싱하고 컴파일한다.
# 2. 스택 기반 인터프리터로 바이트코드를 실행한다.
# 바이트코드 인터프리터는 파이썬 프로그램이 실행되는 동안 지속되고 일관성 있는 상태를 유지한다.
# 파이썬은 전역 인터프리터 잠금(GIL, Global Interpreter Lock)이라는 메커니즘으로 일관성을 유지한다.
# GIL은 상호 배제 잠금(mutax)이며 CPython이 선점형 멀티스레딩의 영향을 받지 않게 막아준다.

# 파이썬도 멀티스레드 지원하지만, GIL은 한 번에 한 스레드만 실행하게 한다.

from time import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [2139079, 1214759, 1516637, 1852285]
start = time()
for number in numbers:
    list(factorize(number))
end = time()
print('Took %.3f seconds' % (end - start))

from threading import Thread


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


# start = time()
# threads = []
# for number in numbers:
#     thread = FactorizeThread(number)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
# end = time()
# print('Took %.3f seconds' % (end - start))

# 멀티스레드를 이용하면 프로그램이 동시에 여러 작업을 하는 것처럼 보이게 만들기가 용이하다.
# 동시에 동작하는 태스크를 관리하는 코드를 직접 구현하기는 어렵다.
# 스레드를 이용하면 함수를 마치 병렬로 실행하는 것처럼 해주는 일을 파이썬에 맡길 수 있다.
# 비록 GIL 때문에 한번에 한 스레드만 진행하지만, CPython은 파이썬 스레드가 어느 정도 공평하게 실행됨을 보장하기 때문이다.

# 특정 유형의 시스템 호출을 수행할 때 일어나는 블로킹 I/O를 다루기 위해서다.
# 시스템 호출(system call)은 파이썬 프로그램에서 외부 환경과 대신 상호 작용하도록 컴퓨터 운영체제에 요청하는 방법이다.
# 블로킹 I/O로는 파일 읽기/쓰기, 네트워크와의 상호작용, 디스플레이 같은 장치와의 통신 등이 있다.
# 스레드는 운영체제가 이런 요청에 응답하는 데 드는 시간을 프로그램과 분리하므로 블로킹 I/O를 처리 할 때 유용하다.
import select


def slow_systemcall():
    select.select([], [], [], 0.1)


# start = time()
# for _ in range(5):
#     slow_systemcall()
# end = time()
# print('Took %.3f seconds' % (end - start))

start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    pass


for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))
