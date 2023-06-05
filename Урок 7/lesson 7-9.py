# композиция - создается класс-контейнер, включающий вызовы других классов
# центральный класс контейнера - комната

class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height)) # передает объекты WindowDoor

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square # берем объект и тянем из него атрибут square
        return main_square

r = Room(7, 4, 3.7)
print(r.square) # --->>> 81.9
r.add_win_door(2, 2) # то, что вычитается из площади (окна и двери)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
print(r.common_square()) # --->>> 69.4

