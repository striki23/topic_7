# Программа выводит пирамиду последовательностей,
# размер которой задает пользователь.
# Каждое число в последовательности должно повторяться столько раз,
# сколько оно само.

rows = int(input('Введите целое положительное число: '))

# Решение с помощью for:
for i in range(1, rows + 1):
    for _ in range(i):
        print(i, end=' ')
    print()

# ------------------------------

i = 1
while i <= rows:
    j = 0
    while j < i:
        print(i, end=' ')
        j += 1
    i += 1
    print()
