# статические методы и методы класса

class MyClass:
    def __init__(self, n_1):
        self.n_1 = n_1

    def m_1(self):
        print("Hi")

    @staticmethod
    def m_2():
        # print("Hello")
        return MyClass(45).n_1 # создан новый безымянный объект, который будет работать через конструктор

first = MyClass(12)
print(first.m_2()) # --->>> 45 (не 12)