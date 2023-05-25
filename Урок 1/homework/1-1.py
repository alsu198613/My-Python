# Поработайте с переменными, создайте несколько, выведите на экран.

person_name = 'Max'
print(person_name)
age = 20
print(age)
period = 1.5
print(period)
is_good = True
print(is_good)
profession = None
print(profession)

# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

name = input('Введите ваше имя: ')
your_age = int(input('Введите ваш возраст: '))
job = input('Кем вы хотите стать: ')
print(f'Ваше имя: {name}, Ваш возраст: {your_age}, Вы хотите стать: {job}')

# Калькулятор
roubles = int(input('Введите сумму в рублях: '))
euro = 115.60
dollar = 104.68

rub_to_euro = roubles / euro
rub_to_dollar = roubles / dollar

print(f'Сумма {roubles:,} рублей = {(round(rub_to_euro, 2))} евро')  # Сумма 200,000,000 рублей
print(f'Сумма {roubles:,} рублей = {rub_to_dollar:,.2f} долларов')
