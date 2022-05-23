# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите кол-во вводимых чисел: '))
number = int(input('Введите цифру: '))

def my_func(number, data):
    if not data:
        return 0
    elif number == data % 10:
        return 1 + my_func(number, data // 10)
    else:
        return 0 + my_func(number, data // 10)

n = int(input('Введите кол-во вводимых чисел: '))
number = int(input('Введите цифру: '))

for i in range(n):
    data = int(input(f'Введите число №{i + 1}: '))
    print(f'Цифра {number} встречается в {data}: {my_func(number, data)}')