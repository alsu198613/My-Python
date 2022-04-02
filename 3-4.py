# первый вариант с помощью оператора **.
def my_func(x, y):
    """
    Функция принимает действительное положительное число x и
    целое отрицательное число y и выполняет возведение числа x в степень y.
    Функции возведения числа в степень не используется.
    :param x:
    :param y:
    :return:
    """
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return 'Значение x должно быть положительным. \nЗначение y должно быть отрицательным.'
        else:
            return x ** y
    except (ValueError, TypeError) as err:
        print(err)


print(my_func(5, -3))


# второй вариант, предусматривающий использование цикла
def my_func_1(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return 'Значение x должно быть положительным. \nЗначение y должно быть отрицательным.'
        else:
            result = 1
            for r in range(abs(y)):
                result /= x
            return result
    except (ValueError, TypeError) as err:
        print(err)


print(my_func_1(5, -3))
