# можно добавить возможность считать количество объектов (машин)

class MyAuto:
    # атрибуты класса убираются при использовании конструктора (для создания разных объектов)
    a_count = 0     # глобальная переменная

   # конструктор
   # атрибуты объекта
    def __init__(self, n, m, y):    # указываются переменные для создания нового объекта
        # чтобы переменные были видны снаружи, используется self
        self.name = n
        self.model = m
        self.year = y
        MyAuto.a_count += 1   # увеличиваем количество машин на 1. Обращаемся к атрибуту класса, а не объекта.

    # методы
    def on_start(self, speed):  # speed - локальная переменная, к ней нельзя получить доступ через self
                                # этот параметр нужно указывать при вызове метода (auto_1.on_start(35))
        print(f"Go-go a car {self.name} with speed {speed}!")

    def on_stop(self):
        print("Stop.")

auto_1 = MyAuto("Mazda", "CX 9", 2022)
print(auto_1.a_count)
auto_1.on_start(35)
# --->>>
# 1
# Go-go a car Mazda with speed 35!

print()
auto_2 = MyAuto("Lexus", "RX 350", 2019)
print(auto_2.a_count)
auto_2.on_start(12)