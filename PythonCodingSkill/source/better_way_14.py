def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 0
try:
    result = divide(x, y)
except ValueError as e:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
