# Программа рисует ромб из звездочек
# по заданной пользователем размерности size
size = int(input())

print('Решение с помощью for:')
# цикл для прорисовки первой половины ромба
for i in range(1, size+1):

    for _ in range(size-i):
        print(' ', end='')
    for _ in range(i*2-1):
        print('*', end='')

    print()

# цикл для прорисовки второй половины ромба
for j in range(1, size):

    for _ in range(j):
        print(' ', end='')
    for _ in range((size*2-1)-(j*2)):
        print('*', end='')

    print()

print('\nРешение с помощью while:')
# цикл для прорисовки первой половины ромба
counter = 1
while counter <= size:

    space = size - counter
    while space > 0:
        print(' ', end='')
        space -= 1

    stars = counter * 2 - 1
    while stars > 0:
        print('*', end='')
        stars -= 1

    print()
    counter += 1

# цикл для прорисовки второй половины ромба
new_counter = 1
while new_counter < size:

    space = new_counter
    while space > 0:
        print(' ', end='')
        space -= 1

    stars = size * 2 - 1 - new_counter*2
    while stars > 0:
        print('*', end='')
        stars -= 1

    print()
    new_counter += 1
