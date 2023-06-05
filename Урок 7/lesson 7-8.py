# геттеры и сеттеры

class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter
    @property
    def age(self): # создаем метод с таким же названием, как приватный атрибут
        return self.__age

    # setter - используется для изменения значения переменной
    @age.setter
    def age(self, n_age):
        if str(n_age).isdigit():
            self.__age = n_age
        else:
            print(f"Age: {n_age} must be positive and integer.")

mc_1 = User("Ivan", 23)
# print(mc_1.__age) # не работает, так как это приватная переменная

print(mc_1.age) # --->>> 23 #
mc_1.age = 23.5 # --->>> Age: 23.5 must be positive and integer.
mc_1.age = -24  # --->>> Age: -24 must be positive and integer.
mc_1.age = 24
print(mc_1.age) # --->>> 24 #
