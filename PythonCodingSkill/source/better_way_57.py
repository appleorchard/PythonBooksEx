def complex_func(a, b, c):
    # ...
    print('start debug')
    import pdb;
    pdb.set_trace()

    a = 1
    b = 2

    print('end debug')


if __name__ == '__main__':
    complex_func(1, 2, 3)
