# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
i_num = number % 10  # остаток от деления на 10
max = 0
# print(i_num)
while number > 0:
    if i_num > max:
        max = i_num
    number //= 10  # number = number // 10  - целочисленное деление
print(max)

#
#
# i = 3481561
# ls = []
# while i > 10:
#     ls.append(i % 10)
#     i //= 10
# r = max(ls)
# print(r)
#
#
# def f(num):
#     m = 0
#     for n in str(num):
#         if int(n) > m:
#             m = int(n)
#     return m
#
#
# def f(num):
#     return int(sorted(str(num))[-1])
