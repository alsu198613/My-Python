# пример проверки возможности покупателя купить машину

class Car:
    def __int__(self, model, price):
        self.model = model
        self.price = price


# композиция
class CarFactory:  # завод по созданию авто
    model = "DeLorean"
    common_price = 5500  # общая цена

    def build(self, count=1):  # количество авто
        cars = []

        for i in range(count):
            cars.append(Car(self.model, self.common_price))
        return cars

class CapacityEx(Exception):
    def __init__(self, current, need):
        self.current = current
        self.need = need

    def __str__(self):
        return f"Not enough space, current = {self.current}, need = {self.need}"


class CarStock:  # склад
    def __init__(self, count=0):
        self.max_count = count
        self.cars = []

    def store(self, cars):
        # проверка вместимости
        self.cars.extend(cars)


class NotEnMoneyEx(Exception):
    def __init__(self, current, need):
        self.current = current
        self.need = need

    def __str__(self):
        return f"Not enough money, current = {self.current}, need = {self.need}"


class Customer:
    def __init__(self, money):
        self.money = money

    def buy(self, car):
        # проверка текущего баланса
        if car.price > self.money:
            raise NotEnMoneyEx(self.money, car.price)
        self.money -= car.price


factory = CarFactory()
stock = CarStock(1)
customer_1 = Customer(2298)

car_list = factory.build(5)  # завод произвел 5 машин
stock.store(car_list)

try:
    customer_1.buy(stock.cars[3])
except NotEnMoneyEx as err:
    print(err, err.need - err.current)

print(customer_1.money)
