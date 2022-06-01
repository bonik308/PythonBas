# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile
from timeit import timeit

def my_func_1(n):
    my_var = 0
    my_data = 1
    for i in range(n):
        #print(f'{my_data}', sep=';', end=' ')
        my_var += my_data
        my_data /= -2
    return my_var

def my_func_main():
    global n
    my_func_1(n)

for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_1(n)",setup="from __main__ import my_func_1, n",number=1000)}')
    cProfile.run("my_func_main()")
