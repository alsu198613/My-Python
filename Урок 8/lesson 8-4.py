# статические методы и методы класса

class MyClass:
    def m_1(self):
        print("Hi")

    @staticmethod
    def m_2():
        # print("Hello")
        return MyClass().m_1() # нужно, чтобы m_2 получил результат работы m-1
# право обращаться к m_1 есть только у объекта
first = MyClass()
first.m_2() # --->>> Hi