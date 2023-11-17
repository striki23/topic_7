# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
row = int(input())
counter = 1

while counter <= row:
    space = row - counter
    while space > 0:
        print(' ', end=' ')
        space -= 1

    stars = 2 * counter - 1
    while stars > 0:
        print('*', end=' ')
        stars -= 1

    print()
    counter += 1
