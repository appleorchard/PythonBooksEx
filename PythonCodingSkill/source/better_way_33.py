# 메타클래스를 응용하는 가장 간단한 사례는 클래스를 올바르게 정의했는지 검증하는 것이다.
# 복잡한 클래스 계층을 만들 때 스타일을 강제하거나 메서드를 오버라이드하도록 요구하거나 클래스 속성 사이에
# 철저한 관계를 두고 싶을 수도 있다.

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


# Python 2
# class MyClassInPython2(object):
#     __metaclass__ = Meta


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # 추상 Polygon 클래스는 검증하지 않음
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons reed 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # 서브클래스에서 설정함

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print(Triangle.interior_angles())

print('Before class')


class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')


print('After class')
