# 키워드 인수의 기본값으로 비정적(non-static) 타입을 사용해야 할 때도 잇다.
from datetime import datetime
from time import sleep


# datetime.now 함수를 정의할 대 딱 한번만 실행
def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Mesage to print
        when: datetime of when the message occurred
            Defaults to the present tme
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log('Hi there!')
sleep(0.1)
log('Hi agin!')

import json


def decode(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary
    """
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is bar




