# Программа выводит фигуру песочные часы из '*'
# Количество рядов половины фигуры задает пользователь в size

size = int(input())

print('Решение с помощью for:')
# прорисовка верхней части песочный часов:
for i in range(size, 0, -1):

    for j in range(size - i):
        print(' ', end='')
    for _ in range(i * 2 - 1):
        print('*', end='')
    print()

# прорисовка нижней части песочный часов:
for x in range(2, size + 1):

    for _ in range(size - x):
        print(' ', end='')
    for _ in range(x * 2 - 1):
        print('*', end='')
    print()

print('\nРешение с помощью while:')
# прорисовка верхней части песочный часов:
counter = 0
while counter < size:
    space = counter
    while space > 0:
        print(' ', end='')
        space -= 1

    stars = size * 2 - 1 - counter*2
    while stars > 0:
        print('*', end='')
        stars -= 1

    counter += 1
    print()

# прорисовка нижней части песочный часов:
new_counter = 2
while new_counter <= size:
    space = size - new_counter
    while space > 0:
        print(' ', end='')
        space -= 1

    stars = new_counter * 2 - 1
    while stars > 0:
        print('*', end ='')
        stars -=1

    new_counter += 1
    print()
