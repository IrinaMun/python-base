"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep


class TrafficLight(object):

    def __init__(self):
        self._colors = ["Красный", "Желтый", "Зеленый"]
        self.delays = [3, 1, 3]
        self.color = None

    def running(self):
        self.color = self._colors[0]

        while True:
            print(self.color)
            sleep(self.delays[self._colors.index(self.color)])
            self.switch()

    def switch(self):
        state = self._colors.index(self.color)
        if state + 1 >= len(self._colors):
            self.color = self._colors[0]
        else:
            self.color = self._colors[state + 1]


if __name__ == '__main__':
    TrafficLight().running()
