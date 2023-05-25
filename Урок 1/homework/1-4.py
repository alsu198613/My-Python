# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
num = number 
max = 0
# print(i_num)
while num > 0:
    last_digit = num % 10 
    if last_digit > max:
        max = last_digit
        if max == 9:  # Это условие не обязательно, но экономит время исполнения. Цифр больше 9 не бывает.
            break
    num //= 10  # number = number // 10  - целочисленное деление
print(max)

# Функция с рекурсией

def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10


print(f"The largest number is: {num_max(int(input('Enter the number: ')))}")

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
