# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

numb = input('Введите число: ')
even_number = 0
odd_number = 0

for i in numb:
    if int(i) % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

print(f'Чётных цифр: {even_number}, Нечётных чисел: {odd_number}')
