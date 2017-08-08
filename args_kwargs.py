def fn(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')

    print('\n', kwargs, sep='')
    for kw in kwargs:
        print(kw)
        print(kwargs[kw])

    for key, value in kwargs.items():
        print(key, value)


fn(10, 4, 2, 6, a=10, c=16, b=7)
