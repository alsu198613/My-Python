# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = input('введите число n: ')
n1 = int(n)
n2 = int(n * 2)
n3 = int(n * 3)
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

n = input("Enter an integer: ")

while n < '0':
    print("I've asked for number greater than 0! Please try again!")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
