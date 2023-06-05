# модификаторы доступа

class MyAuto:
    # конструктор
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self._model = m  # модификаторы доступа (protected -
        # если файл будет использоваться как модуль,
        # то нельзя будет обратиться к этой переменной)
        self.__year = y  # модификаторы доступа (private - можно видеть только в рамках класса)

    # методы
    def on_start(self, speed):
        print(f"Go-go a car {self._model} with speed {speed}!")

    def on_stop(self):
        print(f"Stop a car with year {self.__year}.")  # вызов атрибута private методом

    def get_year(self):  # для получения атрибута private пр внешнем вызове
        return (self.__year)

    def set_year(self, new_year):  # для изменения заданной константы private атрибута
        self.__year = new_year


auto_1 = MyAuto("Mazda", "CX 9", 2022)
auto_1.on_start(35)  # --->>> Go-go a car CX 9 with speed 35!   (protected работает при вызове метода)
print(auto_1._model)  # --->>> CX 9 (внешний вызов тоже работает для protected)

print()
auto_2 = MyAuto("Lexus", "RX 350", 2019)
auto_2.on_stop()  # --->>> Stop a car with year 2019.    (private работает при вызове метода)
# print(auto_2.__year) # 'MyAuto' object has no attribute '__year' (внешний вызов не работает для private)
print(auto_2.get_year())  # --->>> 2019.  Внешний вызов через функцию get. Показывает private атрибут
auto_2.set_year(2023)     # задает новое значение private атрибуту
print(auto_2.get_year())  # --->>> 2023
print(auto_1._MyAuto__year) # --->>> 2022   способ внешнего вывода private атрибута (_Класс__Атрибут)