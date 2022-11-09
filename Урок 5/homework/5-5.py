# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open("test_5.txt", "w", encoding="utf-8") as my_f:
    my_list = [randint(1, 100) for i in range(10)]
    my_f.write(" ".join(map(str, my_list)))

print(f"Сумма чисел в файле - {sum(my_list)}")
