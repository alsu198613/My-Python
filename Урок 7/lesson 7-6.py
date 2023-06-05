# интерфейс итераций

class Iter:
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # метод __iter__ должен возвращать объект-итератор
        return self     # будет возвращать не объект, а сам себя

    # у итератора есть метод __next__
    def __next__(self):
        self.start += 1     # шаг 1
        if self.start <= 5: # граница - 5
            return self.start
        else:
            raise StopIteration     # вызов завершения итерации


# создаем объект
obj_1 = Iter(2)  # перебор начнется с 2
for i in obj_1:
    print(i)

print()
obj_2 = Iter(-2)  # перебор начнется с -2
for i in obj_2:
    print(i)

# 2-й раз запустить итератор уже не получится
print()
for i in obj_1:
    print(i)