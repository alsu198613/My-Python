# Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]

print(reduce(my_func, my_list))

# print(reduce(lambda a, b: a * b, [i for i in range(100, 1001, 2)]))
