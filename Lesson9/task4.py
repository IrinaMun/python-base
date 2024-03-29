"""
4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw()
для каждого элемента.
"""


class Stationery (object):
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Начинаем рисовать ручкой")


class Pencil (Stationery):
    def draw(self):
        print("Запускаем отрисовку карандашом")


class Handle (Stationery):
    def draw(self):
        print("Начинаем рисовать маркером")


if __name__ == '__main__':
    stat_list = [Pen('ручка'), Pencil("карандаш"), Handle("Маркер")]
    for stat in stat_list:
        stat.draw()
