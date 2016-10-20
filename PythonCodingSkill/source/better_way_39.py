# 많은 작업을 동시에 실행하는 파이썬 프로그램에서는 종종 작업들을 조율해줘야 한다.
# 가장 유용한 병행 작업 방식 중 하나는 함수의 파이프라인이다.

# 스레드 안전 생산자 - 소비자 큐(thread-safe producer-consumer queue)로 모델링

from queue import deque
from threading import Lock


def download(item):
    return item


def resize(item):
    return item


def upload(item):
    return item


class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


from threading import Thread
from time import sleep


class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.01)
            except AttributeError:
                return
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

import time

while len(done_queue.items) < 1000:
    sleep(0.1)

for thread in threads:
    thread.in_queue = None

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print('Processed', processed, 'items after polling', polled, 'times')

from queue import Queue

queue = Queue()


def consumer():
    print('Consumer waiting')
    queue.get()
    print('Consumer done')


thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object())
thread.join()
print('Producer done')

queue = Queue(1)


def consumer():
    time.sleep(0.1)
    queue.get()
    print('Consumer got 1')
    queue.get()
    print('Consumer got 2')


thread = Thread(target=consumer)
thread.start()

queue.put(object())
print('Producer put 1')
queue.put(object())
print('Producer put 2')
thread.join()
print('Producer done')

in_queue = Queue()

print('-----------------------')


def consumer():
    print('Consumer waiting')
    work = in_queue.get()
    print('Consumer working')
    # Doing work
    print('Consumer done')
    in_queue.task_done()


Thread(target=consumer).start()

in_queue.put(object())
print('Producer waiting')
in_queue.join()
print('Producer done')

print('-----------------------')


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())
download_queue.close()

download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')

