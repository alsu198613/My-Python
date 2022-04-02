def my_func(first_el, second_el, third_el):
    """
    Функция my_func() принимает три позиционных аргумента и
    возвращает сумму наибольших двух аргументов.
    (number, number) -> number
    Позиционные параметры:
    first_el - первый элемент
    second_el - второй элемент
    third_el - третий элемент
    :return:
    # >>> my_func(2, 3, -4)
    5
    """
    list = [first_el, second_el, third_el]
    result = []
    try:
        first_max = max(list)
        result.append(first_max)
        list.remove(first_max)
        second_max = max(list)
        result.append(second_max)
        print(sum(result))
    except TypeError:
        print('Нужно вводить числа')


my_func(2, 3, -4)
