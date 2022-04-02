def person_data(name, surname, year, city, email, phone):
    """
    Функция принимает параметры как именованные аргументы, описывающие данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Вывод данных о пользователе осуществляется  одной строкой.
    :param name:
    :param surname:
    :param year:
    :param city:
    :param email:
    :param phone:
    :return:
    """
    return f'имя: {name}, фамилия: {surname}, год рождения: {year}, ' \
           f'город: {city}, email: {email}, телефон: {phone}'


print(person_data(name='Иван', surname='Иванов', year=1986, city='Москва',
                  email='info@mail.ru', phone='+71234567'))
