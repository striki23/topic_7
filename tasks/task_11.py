# Программа выводит пирамиду последовательностей,
# размер которой задает пользователь.
# Каждое число в последовательности должно повторяться столько раз,
# сколько оно само.

rows = int(input('Введите целое положительное число: '))

# Решение с помощью for:
#for i in range(rows):
#    for j in range(i+1):
#        print(i+1, end=' ')
#   print()

# Решение с помощью while
# НЕ РАБОТАЕТ!:
i = 0
j = 0
while i < rows:
    while j <= i:
        print(i + 1, end=' ')
        j += 1
    i += 1
    print()

