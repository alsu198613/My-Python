# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    i = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        i += 1
        print(f"{letters} letters in line {i}")
    print(f"String count is {lines}")
