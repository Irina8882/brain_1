def f(pk1, pk2, pk3, *args, **kwargs):
    print(pk1, pk2, pk3, args, kwargs)

f(1, 2, 3, 4, 'test', start='10:00', finish='9:00' )


