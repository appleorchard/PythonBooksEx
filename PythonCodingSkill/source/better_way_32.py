# 파이썬의 언어 후크(language hook)를 이용하면 시스템들을 연계하여 범용 코드를 쉽게 만들 수 있다.
# __getattr__ 이라는 특별한 메서드로 동적 동작을 가능하게 한다.
# 클래스에 __getattr__ 메서드를 정의하면 객체의 인스턴스 딕셔너리에 속성을 찾을 수 없을 때마다 이 메서드가 호출된다.
class LazyDB:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo: ', data.foo)
print('After:', data.__dict__)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print('exists:', data.exists)
print('foo: ', data.foo)
print('foo: ', data.foo)


# 이런 동작은 스키마리스 데이터(schemaless data)에 접근하는 경우에 특히 도움이 된다.

# __getattribute__ 후크. 이 특별한 메서드는 객체의 속성에 접근할 때마다 호출되며,
# 심지어 해당 속성이 딕셔너리에 있을 때도 호출된다. 
# 이런 동작 덕분에 속성에 접근할 때마다 전역 트랜잭션 상태를 확인하는 작업 들에 쓸 수 있다. 
class ValidatingDB:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super(ValidatingDB, self).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


data = ValidatingDB()
print('exists:', data.exists)
print('foo: ', data.foo)
print('foo: ', data.foo)


class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('%s is missing' % name)


# data = MissingPropertyDB()
# data.bad_name

data = LoggingLazyDB()

print('----------------------------------')
print('Before: ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
print('After: ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))

print('----------------------------------')
data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))


class SavingDB:
    def __setattr__(self, name, value):
        # 몇몇 데이터를 DB 로그로 저장함
        super().__setattr__(name, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)


print('----------------------------------')

data = LoggingSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After: ', data.__dict__)
data.foo = 7
print('Finally: ', data.__dict__)


class BronkenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


data = BronkenDictionaryDB({'foo': 3})
data.foo
