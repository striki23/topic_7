# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
size = int(input())
weight = size * 2 - 1
for i in range(size):

    for j in range(i):
        print(' ', end=' ')

    for _ in range(weight):
        print('*', end=' ')
    weight -= 2
    print()

for x in range(1, size):

    for _ in range(1, size-x):
        print(' ', end=' ')

    for _ in range(j):
        print('*', end=' ')
    j += 2
    print()
