# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10% относительно
# предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
# менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.

a = int(input('Введите результат за 1-й день: '))
b = int(input('Введите требуемый результат: '))
i = 1

while a < b:
    a = a + (a * 10 / 100)
    i += 1
    # print(f'{i}, {a:.2f}')

print(f'на {i}-й день спортсмен достиг результата — не менее {b} км')
