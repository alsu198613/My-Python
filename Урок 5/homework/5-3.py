# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
    employees_salary = {line.split()[0]: float(line.split()[1]) for line in f_obj}
    print(f'Average salary = {round(sum(employees_salary.values()) / len(employees_salary), 2)}\n'
          f'Employees with salary less than 20000 {[el[0] for el in employees_salary.items() if el[1] < 20000]}')
