# Программа, которая запрашивает у пользователя число
# и выводит на экран таблицу умножения для этого числа

number = int(input('Введите число: '))

print(f'Таблица умножения для числа {number} с помощью цикла for')
for x in range(1, 11):
    print(number, '*', x, '=', number * x)

print(f'Таблица умножения для числа {number} с помощью цикла while')
x = 1
while x <= 10:
    print(number, '*', x, '=', number * x)
    x += 1
