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

# 2
while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результаты должны быть больше нуля. Стартовое значение != 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьется результат за {days} дней")
        break