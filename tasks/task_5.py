# Программа, которая запрашивает у пользователя число number
# и выводит на экран факториал этого числа
# number должно быть больше 1
number = int(input('Введите число: '))

if number < 0:
    print('Факториал определен только для натуральных чисел.')
else:
    composition = 1
    x = 1
    while x <= number:
        composition *= x
        x += 1
    print(f'Факториал числа {number} равен {composition}')

# Вариант цикла с помощью for:
#     composition = 1
#     for x in range (1, number + 1):
#         composition *= x
#     print(f'Факториал числа {number} равен {composition}')
