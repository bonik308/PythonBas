# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите кол-во элементов: '))
sum  = 0
data = 1

for i in range(n):
    print(f'{data}', sep=';', end = ' ')
    sum += data
    data /= -2
print(f'\n{sum}')