import json


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self, *args, **kwargs):
        return 'Point2D(%d, %d)' % (self.x, self.y)


point = Point2D(5, 3)
print('Object: ', point)
print('Serialzied: ', point.serialize())


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self, *args, **kwargs):
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


point = BetterPoint2D(5, 3)
print('Before: ', point)
data = point.serialize()
print('Serialized: ', data)
after = BetterPoint2D.deserialize(data)
print('After: ', after)


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self, *args, **kwargs):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(str(x) for x in self.args)
        )


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(target_class):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class EvenBetter2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


register_class(EvenBetter2D)

print('----------------------------')
point = EvenBetter2D(5, 3)
print('Before: ', point)
data = point.serialize()
print('Serialized: ', data)
after = deserialize(data)
print('After: ', after)

print('----------------------------')


# class Point3D(BetterSerializable):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# point = Point3D(5, 8, -4)
# data = point.serialize()
# deserialize(data)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class RegistredSerializable(BetterPoint2D, metaclass=Meta):
    pass


class Vector3D(RegistredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z


v3 = Vector3D(10, -7, 3)
print('Before: ', v3)
data = v3.serialize()
print('Serialized: ', data)
print('After: ', deserialize(data))
