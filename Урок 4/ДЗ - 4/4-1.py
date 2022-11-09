# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv


def wages():
    try:
        name, work_per_hour, rate_per_hour, premium = argv
        work_per_hour = float(work_per_hour)
        rate_per_hour = float(rate_per_hour)
        premium = float(premium)
        print(f'Заработная плата сотрудника: {work_per_hour * rate_per_hour + premium}')
    except ValueError:
        print('Введите значение в цифрах.')


wages()
