number = int(input())

for i in range(1, number + 1):

    for _ in range(i):
        print('*', end=' ')

    for _ in range(number*2-i*2):
        print(' ', end=' ')

    for _ in range(i):
        print('*', end=' ')
    print()

for j in range(number, 0, -1):

    for _ in range(j):
        print('*', end=' ')

    for _ in range(number*2-j*2):
        print(' ', end=' ')

    for _ in range(j):
        print('*', end=' ')
    print()