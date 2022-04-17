# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

str_list = []
while True:
    data = input("Введите данные: ")
    if data == '':
        print(str_list)
        exit()
    else:
        new_line = data + '\n'
        str_list.append(new_line)

    with open("text_1.txt", "w", encoding='utf-8') as f_obj:
        f_obj.writelines(str_list)

# with open('text_1.txt', 'r') as f_obj:
#     content = f_obj.read()
#     print(content)
