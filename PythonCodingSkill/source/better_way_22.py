class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 'Math', 90)
book.report_grade('Isaac Newton', 'Math', 50)
book.report_grade('Isaac Newton', 'Gym', 50)
book.report_grade('Isaac Newton', 'Gym', 50)

print(book.average_grade('Isaac Newton'))

# 클래스 리팩토링
# 간단한 정보를 담기에 클래스는 너무 무겁고 튜플이 적당해 보인다.
# 일반적인 튜플의 문제는 위치에 의존한다는 점이다.
# 튜플을 점점 더 길게 확장하는 패턴은 딕셔너리의 계층을 깊게 두는 방식과 비슷하다.
# 튜플의 아이템이 두 개를 넘어가면 다른 방법을 고려해야 한다.

from collections import namedtuple
# namedtuple은 작은 불변 데이터 클래스(immutable data class)
Grade = namedtuple('Grade', ('score', 'weight'))


# namedtuple 의 단점
# 1. namedtuple로 만들 클래스에 기본 인수 값을 설정할 수 없다. 그래서 데이터에 선택적인 속성이 많으면
# 다루기 힘들어진다. 속성을 사용할 때는 클래스를 직접 정의하는게 나을 수 있다.
# 2. namedtuple 인스턴스의 속성 값을 여전히 숫자로 된 인덱스와 순회 방법으로 접근할 수 있다.
# 특히 API로 노출한 경우에는 의도와 다르게 사용되어 나중에 실제 클래스로 바꾸기 더 어려울 수도 있다.
# namedtuple 인스턴스를 사용하는 방식을 모두 제어할 수 없다면 클래스를 직접 정의하는게 낫다.

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = GradeBook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(100, 0.80)
math.report_grade(50, 0.20)

print(albert.average_grade())


