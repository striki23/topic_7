# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
row = int(input())

print("\nРешение с помощью while:")
i = 1
number = 1
while i <= row:
    j = 1
    while j <= i:
        print(number, end=' ')
        j += 1
        number += 1

    i += 1
    print()

print('\nРешение с помощью for:')
number = 1
for i in range(1, row+1):
    for _ in range(i):
        print(number, end=' ')
        number += 1
    print()
