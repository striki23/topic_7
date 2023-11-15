# Программа раскладывает число на простые множители
number = int(input('Введите число: '))

lst = []
multiplier = 2

while multiplier <= number:
    if number % multiplier == 0:
        lst.append(multiplier)
        # print(multiplier, end=' ')
        number = number // multiplier
    else:
        multiplier += 1
print(*lst)
