# Программа выводит на экран все четные числа
# в заданном пользователем диапазоне
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

# обрабатываем случай когда начало диапазона меньше конца

# ПОДСКАЗКА: Тема 4 Задание №2 либо
# можете использовать функции min и max


for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
    elif start == end and start % 2 != 0:
        print(0)
