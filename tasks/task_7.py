# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
# не получается (до конца не понимаю разложение на простые множители)!!!
number = int(input('Введите число: '))
lst = []
multiplier = 2
temp = number
while temp % multiplier != 1:
    temp = temp / multiplier
    lst.append(multiplier)
    multiplier += 1
print(lst)
