# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

my_list = [randint(1,100) for i in range (10)]

print(f'Массив: {my_list}')
a = max(my_list)
b = min(my_list)
print(f'Max: {a}\n'
      f'Min: {b}')
index_a = my_list.index(a)
index_b = my_list.index(b)
my_list[index_a],my_list[index_b] = my_list[index_b],my_list[index_a]
print(f'Измененный массив: {my_list}')