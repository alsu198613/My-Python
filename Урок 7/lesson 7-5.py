# интерфейс итераций

class Iterator:
    """
    Объект-итератор
    """

    def __init__(self, start=0):    # 0 - начало итерации
        self.i = start

    # у итератора есть метод __next__
    def __next__(self):
        self.i += 1     # шаг 1
        if self.i <= 5: # граница - 5
            return self.i
        else:
            raise StopIteration     # вызов завершения итерации


class IterObj:
    """
    Объект, поддерживающий интерфейс итерации (итерируемый объект)
    """

    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # метод __iter__ должен возвращать объект-итератор
        return Iterator(self.start)

# создаем объект
obj_1 = IterObj(2)  # перебор начнется с 2
for i in obj_1:
    print(i)

# итератор можно запустить только 1 раз, но есть лозейка, которой не будет в следущем слайде
print()
for i in obj_1:
    print(i)