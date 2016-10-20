# try, except, else, finally

# 코드를 정리할 필요가 있을 경우는 try/finally를 사용한다.
handle = open('tmp/random_data.txt')  # IOError
try:
    data = handle.read()
finally:
    handle.close()

# 코드에서 어떤 예외를 처리하고 어떤 예외를 전달할지를 명확하게 하려면 try/except/else를 사용해야 한다.
import json


def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]


# 복합문 하나로 모든 것을 처리하고 싶다면 try/except/else/finally를 사용한다.
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')  # IOError가 일어날 수 있음
    try:
        data = handle.read()  # UnicodeDecodeError가 일어날 수 있음
        op = json.loads(data)  # ValueError가 일어날 수 있음
        value = (
            op['numerator'] /
            op['denominator'])  # ZeroDivisionError가 일어날 수 있음
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # IOError가 일어날 수 있음
        return value
    finally:
        handle.close()
