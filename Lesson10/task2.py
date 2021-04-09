"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
(используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:

для пальто: (size*6.5 + 0.5)
для костюма: (2*height + 0.3)
Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка,
используя свойство cloth_size.

Например:

30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (height: 2)
...
Итого: 250.3
"""
from abc import ABC, abstractmethod
from random import randrange


class Clothes(object):
    @property
    def cloth_size(self):
        return 0

    @abstractmethod
    def get_size(self):
        pass

    @classmethod
    def get_type(cls):
        return cls.__name__


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_size(self):
        return 2 * self.size + 0.3

    def get_size(self):
        return self.size


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_size(self):
        return self.height / 6.5 + 0.5

    def get_size(self):
        return self.height


if __name__ == '__main__':
    variants = [Coat, Suit]
    all_clothes = []
    for count in range(10):
        cloth_to_add = variants[randrange(2)]
        if cloth_to_add.get_type() == 'Coat':
            cloth_to_add = cloth_to_add(randrange(42, 60, 2))
        elif cloth_to_add.get_type() == 'Suit':
            cloth_to_add = cloth_to_add(randrange(160, 180))
        all_clothes.append(cloth_to_add)

    for cloth in all_clothes:
        print(f'{round(cloth.cloth_size, 2)} - {cloth.get_type()} ({cloth.get_size()})')

    print(f'Итого: {round(sum([i.cloth_size for i in all_clothes]), 2)}')
