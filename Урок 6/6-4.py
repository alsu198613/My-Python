# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

from random import choice


class Car:
    direction = ["на север", "на юг", "на восток", "на запад"]

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'Машина: {name}, имеет цвет: {color}.\nЭто полицейская машина? {is_police}')

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Скорость машины- {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость машины- {self.speed}. Превышение скорости!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость машины- {self.speed}. Превышение скорости!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


town_car = TownCar('Лада', 'жёлтый', 65)
work_car = WorkCar('Газель', 'синий', 40)
sport_car = SportCar('Porsche', 'красный', 120)
police_car = PoliceCar('ДПС', 'белый', 80)

list_of_cars = [town_car, work_car, sport_car, police_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
