start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

result = []
if start == end or start < 0 or end < 0:
    print('Некорректный диапазон')
else:
    if start > end:
        start, end = end, start

    for number in range(start, end + 1):

        str_number = str(number)
        is_armstrong = 0
        for num in str_number:
            is_armstrong += int(num) ** len(str_number)

        if is_armstrong == number:
            result.append(number)

    print(*result)
