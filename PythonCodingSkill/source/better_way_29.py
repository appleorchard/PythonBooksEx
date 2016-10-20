class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After: %5r' % r0.get_ohms())

# 즉석에서 증가시키기 같은 연산에는 사용하기 불편
r0.set_ohms(r0.get_ohms() + 5e3)
print(r0.get_ohms())


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
print('%r ohms, %r volts, %r amps' % (r1.ohms, r1.voltage, r1.current))

# 즉석에서 증가시키기 연산이 자연스럽고 명확해진다.
r1.ohms += 5e3


# 속성을 설정할 때 특별한 동작이 일어나야 하면 @property 데코레이터(decorator)와 이에 대응하는 setter 속성을 사용하는 방법으로 바꿀 수 있다.
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After: %5r amsp' % r2.current)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


# r3 = BoundedResistance(-1)


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
r4.ohms = 2e4


# @property의 가장 큰 단점은 속성에 대응하는 메서드를 서브클래스에서만 공유할 수 있다는 점이다.
class MysteriousResitor(Resistor):
    @property
    def ohms(self):
        self.votage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


# 게터 프로퍼티 메서드에서 다른 속성을 설정하지 말아야 한다.
r7 = MysteriousResitor(10)
r7.current = 0.01
print('Before: %5r' % r7.voltage)
r7.ohms
print('After: %5r' % r7.voltage)
# 최선의 정책은 @property.setter 메서드에서만 관련 객체의 상태를 수정하는 것이다.
# 모듈을 동적으로 임포트하거나, 느린 헬퍼 함수를 실행하거나, 비용이 많이 드는 데이터베이스 쿼리를 수행하는 일처럼
# 호출하는 쪽이 객체에서 일어날 것이라고 예측하지 못할 만한 다른 부작용은 모두 피해야 한다.
#
# 사용자는 다른 파이썬 객체가 그렇듯이 클래스의 속성이 빠르고 쉬울 거라고 기대할 것이다.
# 더 복잡하거나 느린 작업은 일반 메서드로 하자.
