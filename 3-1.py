def divider(a, b):
    """
    Функция принимает два числа от пользователя и выполняет их деление
    (number, number) -> number
    Позиционные параметры:
    a -- делимое
    b -- делитель
    # >>> divider(10, 5)
    2.0
    """

    c = a / b
    return c


try:
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    print(round(divider(a, b), 2))
except (ZeroDivisionError, ValueError) as err:
    print(err)
