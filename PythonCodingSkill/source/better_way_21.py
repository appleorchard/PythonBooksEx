def safe_division(number, divisor,
                  *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# result = safe_division(1, 10 ** 500, True, False)
# print(result)
#
# result = safe_division(1, 0, False, True)
# print(result)

result = safe_division(1, 10 ** 500, ignore_overflow=True)
print(result)

result = safe_division(1, 0, ignore_zero_division=True)
print(result)


def print_args(*args, **kwargs):
    print('Positional: ', args)
    print('Keyword: ', kwargs)


print_args(1, 2, foo='bar', stuff='meep')


def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)

    if kwargs:
        raise TypeError('Unexpeced **kwargs: %r' % kwargs)


safe_division_d(1, 10)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10 ** 500, ignore_overflow=True)

# safe_division_d(1, 0, True, False)
