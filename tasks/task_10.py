# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

# Некорректно работает условия: выбрасывается ошибка если числа равны или равны 0
result = []
if start > end:
    start, end = end, start
elif start == end or start < 0 or end < 0:
    print('Некорректный диапазон')
for number in range(start, end + 1):
    str_number = list(str(number))
    is_armstrong = 0
    for num in str_number:
        is_armstrong += int(num) ** len(str_number)
    if is_armstrong == number:
        result.append(number)
print(*result)