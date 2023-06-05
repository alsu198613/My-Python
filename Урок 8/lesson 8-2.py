# статические методы и методы класса

class MyClass:
    def m_1(self):
        # print("Hi")
        return self.m_2() # функция обращается к результатам работы m_1

    @staticmethod
    def m_2():
        print("Hello")


first = MyClass()
first.m_1() # --->>> Hello