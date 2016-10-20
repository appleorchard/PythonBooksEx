class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


#
#
# class MyChildClass(MyBaseClass):
#     def __init__(self):
#         MyBaseClass.__init__(self, 5)
#
#
# class TimeTwo(object):
#     def __init__(self):
#         self.value *= 2
#
#
# class PlusFive(object):
#     def __init__(self):
#         self.value += 5
#
#
# class OneWay(MyBaseClass, TimeTwo, PlusFive):
#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         TimeTwo.__init__(self)
#         PlusFive.__init__(self)
#
#
# foo = OneWay(5)
# print('First ordering is (5 * 2) + 5 = ', foo.value)
#
#
# class AnotherWay(MyBaseClass, PlusFive, TimeTwo):
#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         TimeTwo.__init__(self)
#         PlusFive.__init__(self)
#
#
# bar = AnotherWay(5)
# print('Second ordering still is', bar.value)


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)


# 파이썬 2.2에서는 이 문제를 해결하려고 super라는 내장 함수를 추가하고 메서드 해석 순서(MRO, Method Resolution Order)를 정의했다.
# MRO는 어떤 슈퍼클래스로부터 초기화하는지를 정한다(예를 들면 깊이 우선, 왼쪽에서 오른쪽으로). 또한 다이아몬드 계층 구조에 있는 공통 슈퍼클래스를 단 한번만 실행하게 된다.
class TimeFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimeFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimeFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35 and is ', foo.value)

from pprint import pprint

pprint(GoodWay.mro())


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value
