# Исходный список чисел
numbers = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

# создаем пустой список, в который будем добавлять
# числа списка, соответствующие требованию
result = []
for x in numbers:
    x = int(x)
    if ((x % 5 == 0) or (x % 7 == 0)) and x > 100:
        result.append(x)
print('Числа, кратные 5 или 7 и больше 100:', *result)
