# декоратор @property - делает так, что мы работаем с методом, как с атрибутом

class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def my_method(self):
        return f"Параметры, переданные в класс:" \
               f" {self.param_1}, {self.param_2}"

mc = MyClass("text_1", "text_2")

print(mc.param_1)
print(mc.param_2)
print(mc.my_method) # метод указывается без (), т.е. как атрибут
