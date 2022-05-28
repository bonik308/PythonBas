# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

my_list = [randint(1, 100) for _ in range(10)]
print(f'Список: {my_list}')

min_1 = min(my_list)
my_list.remove(min_1)
min_2 = min(my_list)
print(f'Два наименьших элемента: {min_1,min_2}')