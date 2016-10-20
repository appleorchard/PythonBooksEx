class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = Homework()
galileo.grade = 95


class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


# 디스크립터 클래스는 반복 코드 없이도 성적 검증 동작을 재사용할 수 있게 해주는 __get__과 __set__ 메서드를 제공할 수 있다.
# 이런 목적으로는 디스크립터가 믹스인보다도 좋은 방법이다.
# 디스크립터를 이용하면 한 클래스의 서로 다른 많은 속성에 같은 로직을 재사용할 수 있기 대문이다.
# class Grade(object):
#     def __get__(*args, **kwargs):
#         pass
#
#     def __set__(*args, **kwargs):
#         pass
class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40

Exam.__dict__['writing_grade'].__set__(exam, 40)
print(exam.writing_grade)


# Exam 인스턴스에 writing_grade 속성이 없으면 파이썬은 대신 Exam 클래스의 속성을 이용한다.
# 이 클래스의 속성이 __get__과 __set__ 메서드를 갖춘 객체라면 파이썬은 디스크립터 프로토콜을 따른다고 가정한다.
from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


# 남아있는 문제는 메모리 누수다.
# _values 딕셔너리는 프로그램의 수명 동안 __set__에 전달된 모든 Exam 인스턴스의 참조를 저장한다.
# 결국 인스턴스의 참조 개수가 절대로 0이 되지 않아 가비지 컬렉터가 정리하지 못하게 된다.
# 파이썬 내장 모듈 weakref를 사용해서 이 문제를 해결할 수 있다.


class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 83
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)

second_exam = Exam()
second_exam.writing_grade = 75
print('Second', second_exam.writing_grade, 'is right')
print('First', first_exam.writing_grade, 'is wrong')

# 문제는 한 Grade 인스턴스가 모든 Exam 인스턴스의 writing_grade 클래스 속성으로 공유된다는 점이다.
# 이 속성에 대응하는 Grade 인스턴스는 프로그램에서 Exam 인스턴스를 생성할 때마다 생성되는 게 아니라
# Exam 클래스를 처음 정의할 때 한 번만 생성된다.
