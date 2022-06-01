# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile
from timeit import timeit

def my_func_1(n):
    my_list = [i for i in range(n)]
    my_list[1] = 0
    m = 2
    while m < n:
        if my_list[m] != 0:
            j = m * 2
            while j < n:
                my_list[j] = 0
                j = j + m
        m += 1
    return [i for i in my_list if i != 0]

def my_func_main():
    global n
    my_func_1(n)

for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_1(n)",setup="from __main__ import my_func_1, n",number=1000)}')
    cProfile.run("my_func_main()")