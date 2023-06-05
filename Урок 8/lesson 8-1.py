# статические методы и методы класса

class MyClass:
    def m_1(self):
        print("Hi")

    @staticmethod
    def m_2(): # это функция в теле класса, скобки могут быть пустыми
        print("Hello")


first = MyClass()
# first.m_1() # --->>> Hi
# MyClass.m_1() # --->>> TypeError: m_1() missing 1 required positional argument: 'self'
MyClass.m_1(first) # --->>> Hi
MyClass.m_1(12) # --->>> Hi # нечестный метод

MyClass.m_2() # --->>> Hello # взаимодействие через класс, может вызываться даже без наличия объекта first
first.m_2() # --->>> Hello # взаимодействие через объект