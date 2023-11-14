# Программа выводит на экран все четные числа
# в заданном пользователем диапазоне
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

# обрабатываем случай когда начало диапазона больше конца
if start > end:
    start, end = end, start

for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
    elif start == end:
        print(0)
