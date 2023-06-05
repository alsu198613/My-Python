# множественное наследование
# один родитель и несколько потомков: потомок может работать с родительским методом и со своим,
# но не с методом другого потомка (класс Auto и Bus не видят методов друг друга)
class Transport:
   def transport_method(self):
       print("Родительский метод класса Transport")

class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")

class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")

a = Auto()
a.transport_method() # --->>> Родительский метод класса Transport
b = Bus()
b.transport_method() # --->>> Родительский метод класса Transport

# несколько родителей и один потомок
class Player():
    def player_method(self):
        print("Родительский метод класса Player")

class Navigator():
    def navigator_method(self):
        print("Родительский метод класса Navigator")

class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")

# чтобы так работало в реальности, нужно, чтобы у обоих родителей были одинаковые конструкторы
class Shape():
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"

class Material():
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"

class Triangle(Shape, Material):
    pass

t = Triangle(10, 20)
print(t.get_params()) # --->>> Параметры Shape: 10, 20
# (названия методов одинаковые (get_params), поэтому выводится первый по порядку)


