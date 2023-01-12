try:
    x = int(input('x->'))
    y = int(input('y->'))
    for i in range(0, x):
        for j in range(0, y):
            print('*', end=" ")
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')