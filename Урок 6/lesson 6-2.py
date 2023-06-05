# чтобы каждый раз создавался новый автомобиль нужно использовать конструктор

class MyAuto:
    # атрибуты класса убираются при использовании конструктора (для создания разных объектов)
    # name = "Lexus"
    # model = "RX 350"
    # year = 2022

    # конструктор - метод, который участвует в создании объекта (new, потом init).
    # он собирает необходимые значения для работы объекта
    # атрибуты объекта
    def __init__(self, n, m, y):    # указываются переменные для создания нового объекта
        # чтобы переменные были видны снаружи, используется self
        self.name = n
        self.model = m
        self.year = y
        print(n, m, y)  # может вывести значение всех атрибутов объекта при внешнем вызове
                        # (auto_1 = MyAuto("Mazda", "CX 9", 2022))
        self.on_start() # для каждой машины при создании она сразу начинает ехать.
                        # Не нужно использовать внешний вызов auto_1.on_start().
                        # Только создать объект auto_1 = MyAuto("Mazda", "CX 9", 2022)
                        # Mazda CX 9 2022
                        # Go-go a car Mazda!
    # методы
    # чтобы персонализировать метод, нужно обратиться к переменной. Внутри обращение только через self
    def on_start(self):
        print(f"Go-go a car {self.name}!")
        # self.on_stop()  # Mazda CX 9 2022
                          # Go-go a car Mazda!
                          # Stop.

    def on_stop(self):
        print("Stop.")

auto_1 = MyAuto("Mazda", "CX 9", 2022)
# print(auto_1.name)
# auto_1.on_start()

print()
auto_2 = MyAuto("Lexus", "RX 350", 2019)
# print(auto_2.name)
# auto_2.on_start()