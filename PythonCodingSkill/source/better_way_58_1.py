def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


# def insert_value(array, value):
#     """비효율적인 함수"""
#     for i, existing in enumerate(array):
#         if existing > value:
#             array.insert(i, value)
#             return
#     array.append(value)

from bisect import bisect_left


def insert_value(array, value):
    """bisect를 이용해서 개선된 함수"""
    i = bisect_left(array, value)
    array.insert(i, value)


from random import randint

max_size = 10 ** 4
print(max_size)
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

from cProfile import Profile

profiler = Profile()
profiler.runcall(test)

from pstats import Stats

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()