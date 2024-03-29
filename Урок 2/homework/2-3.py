# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasons = {'зима': (1, 2, 12),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)}

if month <= 0 or type(month) != int:
    print('Ошибка. Введите месяц в виде целого числа от 1 до 12')

# dict
for key in seasons.keys():
    if month in seasons[key]:
        print(f'Данный месяц относится к сезону {key}')

# list
seasons_list = list(seasons.keys())
if month in [12, 1, 2]:
    print(f'Данный месяц относится к сезону {seasons_list[0]}')
elif month in [3, 4, 5]:
    print(f'Данный месяц относится к сезону {seasons_list[1]}')
elif month in [6, 7, 8]:
    print(f'Данный месяц относится к сезону {seasons_list[2]}')
elif month in [9, 10, 11]:
    print(f'Данный месяц относится к сезону {seasons_list[3]}')
else:
    print('Ошибка. Введите месяц в виде целого числа от 1 до 12')
