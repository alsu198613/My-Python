# метод класса (@classmethod) - принимает класс (cls) в качестве первого параметра

class MyClass:
    def __init__(self, n_1):
        self.n_1 = n_1

    def m_1(self):
        print("Hi")

    @staticmethod # позволяет не создавать объекты, а работать через класс
    def m_2():
        print("Hello")

    # метод класса привязывается к самому классу, а не к его экземпляру
    @classmethod # используется как фабрика для создания объектов
    def m_3(cls):
        # print(cls)
        return cls.m_2() # m_3 будет использовать работу m_2
        # cls - это MyClass
first = MyClass(12)
MyClass.m_3() # ---> Hello