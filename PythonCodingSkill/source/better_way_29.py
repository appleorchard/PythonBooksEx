class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


# r1 = Resistor(50e3)
# r1.ohms = 10e3
# r1.ohms += 5e3

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


# r2 = VoltageResistance(1e3)
# print('Before: %5r amps' % r2.current)
# r2.voltage = 10
# print('After: %5r amps' % r2.current)


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


# r3 = BoundedResistance(1e3)
# r3.ohms = 0
# BoundedResistance(-5)

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


# r4 = FixedResistance(1e3)
# r4.ohms = 2e3

class MysteriousResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r5 = MysteriousResistor(10)
r5.current = 0.01
print('Before: %5r' % r5.voltage)
r5.ohms
print('After: %5r' % r5.voltage)
