# Программа выводит пирамиду из '*', вершиной вверх
# количество рядов задает пользователь

row = int(input())
counter = 1

print('Решение через while')
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

print('\nРешение через for:')

for i in range(1, row + 1):
    for _ in range(row - i):
        print(' ', end=' ')

    for _ in range(2 * i - 1):
        print('*', end=' ')

    print()
