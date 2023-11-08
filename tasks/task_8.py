# Программа выводит на экран все четные числа
# в заданном пользователем диапазоне
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

# обрабатываем случай когда начало диапазона меньше конца
if start < end:
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

# обрабатываем случай когда начало диапазона больше конца
elif start > end:
    for number in range(end, start + 1):
        if number % 2 == 0:
            print(number)

# обрабатываем случай когда начало и конец диапозона равны
else:
    if start == end and start % 2 == 0:
        print(start)
    elif start == end and start % 2 != 0:
        print(0)
