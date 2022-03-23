# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
seconds %= 3600  # seconds = seconds % 3600
minutes = seconds // 60
seconds %= 60  # seconds = seconds % 60
print('%02d:%02d:%02d' % (hours, minutes, seconds)) # print(f'{hours}:{minutes}:{seconds}') не выводит 01
