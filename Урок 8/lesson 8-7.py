# метод класса (@classmethod) - принимает класс (cls) в качестве первого параметра
# реальный вариант

class MyClass:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    # @staticmethod # позволяет не создавать объекты, а работать через класс
    # def m_2():
    #     print("Hello")
    #
    # метод класса привязывается к самому классу, а не к его экземпляру
    # может работать как альтернативный конструктор
    @classmethod # используется как фабрика для создания объектов
    def set_fio(cls, data):
        n, s = data
        return cls(n, s) # m_3 будет использовать работу m_2
        # cls - это MyClass

my_list = ["N", "S"]

first = MyClass.set_fio(my_list)
print(first.name) # --->>> N

# идеальный вариант

# class MyClass:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
#     # @staticmethod # позволяет не создавать объекты, а работать через класс
#     # def m_2():
#     #     print("Hello")
#     #
#     # # метод класса привязывается к самому классу, а не к его экземпляру
#     # @classmethod # используется как фабрика для создания объектов
#     # def m_3(cls):
#     #     # print(cls)
#     #     return cls.m_2() # m_3 будет использовать работу m_2
#     #     # cls - это MyClass
#
#
# first = MyClass("N", "S")
# print(first.name) # --->>> N