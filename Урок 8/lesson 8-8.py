# метод класса (@classmethod) - принимает класс (cls) в качестве первого параметра
# реальный вариант + @staticmethod

class MyClass:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    @staticmethod # позволяет не создавать объекты, а работать через класс
    def get_fio(obj):
        return f"{obj.name} {obj.surname}"

    @classmethod
    def set_fio(cls, data):
        n, s = data
        return cls(n, s)

my_list = ["N", "S"]

first = MyClass.set_fio(my_list)
print(MyClass.get_fio(first)) # --->>> N

#############################################
class MyClass:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.get_fio(name, surname)

    @staticmethod # позволяет не создавать объекты, а работать через класс
    def get_fio(n, s):
        return f"{n} {s}"

    @classmethod
    def set_fio(cls, data):
        n, s = data
        return cls(n, s)

my_list = ["N", "S"]

first = MyClass.set_fio(my_list)
print(MyClass.get_fio(first)) # --->>> N
