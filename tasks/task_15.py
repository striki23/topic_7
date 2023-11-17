# Программа рисует ромб из звездочек
# по заданной пользователем размерности size

size = int(input())
counter = 1
stars = 1

# цикл для прорисовки первой половины ромба

for i in range(size):

    space = size - counter
    for j in range(space):
        print(' ', end=' ')
        space -= 1

    for _ in range(0, stars):
        print('*', end=' ')
    stars += 2

    print()
    counter += 1

#уменьшаем количество звезд после последнего цикла

stars -= 2

# цикл для прорисовки второй половины ромба
for x in range(1, size):

    space += 1
    for _ in range(space):
        print(' ', end=' ')

    stars -= 2
    for _ in range(stars):
        print('*', end=' ')

    print()
