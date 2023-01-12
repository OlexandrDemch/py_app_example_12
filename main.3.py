try:
    col = int(input('col->'))
    for i in range(0, col):
        for j in range(0, col):
            if i == 0 or i == col-1:
                print('*', end=" ")
            else:
                if j == 0 or j == col - 1:
                    print('*', end=" ")
                else:
                    print(' ', end=" ")
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
