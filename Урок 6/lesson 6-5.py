# наследование
class Transport:        # атрибуты и методы, характерные для всех типов транспорта
    # конструктор
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y

    # методы
    def on_start(self, speed):
        print(f"Go-go a car {self.name} with speed {speed}!")

    def on_stop(self):
        print("Stop.")

class MyAuto(Transport):    # указываем родителя, куда обращаться за атрибутами и методами
    def __init__(self, n, m, y, p):  # если вносятся изменения в родительский конструктор, например, нужен
                                     # новый параметр, то прописать def __init__(-//-, p) с добавлением изменений
        super().__init__(n, m, y)    # и указать, что старые родительские атрибуты не меняются (super().__init__)
        self.pas = p

    def drift(self):
        print("Vgggggg")


auto_1 = MyAuto("Mazda", "CX 9", 2022, 7) # если у родителя есть конструктор, то потомки обязаны передавать в него данные
auto_1.on_start(35)  # --->>> Go-go a car Mazda with speed 35!
auto_1.drift()       # Vgggggg
print()
auto_2 = MyAuto("Lexus", "RX 350", 2019, 7)
print(auto_2.name)   # Lexus
auto_2.on_start(12)  # Go-go a car Lexus with speed 12!