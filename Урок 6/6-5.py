# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title="канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. Результат: {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Напишите ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Напишите карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Напишите маркером {self.title}")


stat = Stationery()
pen = Pen("Parker")
pencil = Pencil("BIC")
handle = Handle("ErichKrause")

office_supplies = [stat, pen, pencil, handle]

for i in office_supplies:
    i.draw()

