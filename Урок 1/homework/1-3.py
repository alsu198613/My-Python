# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = int(input('введите число n: '))
n1 = n
n2 = int(str(n) * 2)
n3 = int(str(n) * 3)
print(n1 + n2 + n3)

# nn = n * 10 + n
# nnn = n * 100 + nn
# print(n + nn + nnn)
#
#
# def solve(n):
#    n1 = n
#    n2 = int(str(n) * 2)
#    n3 = int(str(n) * 3)
#    print(n1 + n2 + n3)
#
#
# solve(33)
