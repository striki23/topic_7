# Программа раскладывает число на простые множители
number = int(input('Введите число: '))
lst = []

multiplier = 2

while number/multiplier >= 1:
    temp = number / multiplier
    if number % multiplier == 0:
        lst.append(multiplier)
        number = temp
    else:
        multiplier += 1
print(*lst)
