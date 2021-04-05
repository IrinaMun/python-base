"""
5. Реализуйте базовый класс Car.
при создании класса должны быть переданы атрибуты: color (str), name (str).
реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины - для хранения
этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль
полицейским (см.дальше)
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет, текущую скорость
автомобиля и направление движения (в случае если автомобиль едет), для полицейских автомобилей перед названием
автомобиля должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций, для каждого автомобиля сделайте одно
из случайных действий: go, stop, turn со случайными параметрами. После каждого действия показывайте статус автомобиля.
"""
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randrange

directions = ['Север', 'Юг', 'Запад', 'Восток']


class Car(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0
        self.direction = None

    def go(self, speed, direction=None):
        self.speed = speed
        if direction:
            self.direction = direction

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        return self.speed

    def is_police(self):
        return False

    def get_status(self):
        status_str = f'Скорость: {self.show_speed()}\n' \
                     f'Цвет: {self.color}\n' \
                     f'Название: {self.name}\n' \
                     f'Направление: {self.direction}\n' \
                     f'*********************************'

        return status_str


class TownCar(Car):
    def show_speed(self):
        result = ''
        if self.speed > 60:
            result += 'ПРЕВЫШЕНИЕ: '
        result += str(self.speed)
        return result


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        result = ''
        if self.speed > 40:
            result += 'ПРЕВЫШЕНИЕ: '
        result += str(self.speed)
        return result


class PoliceCar(Car):
    def is_police(self):
        return True

    def get_status(self):
        result = "POLICE: " + super().get_status()
        return result


if __name__ == '__main__':

    town_car = TownCar(
        color="Green",
        name="Nissan",
    )

    sport_car = SportCar(
        color="Red",
        name="lamborghini",
    )

    work_car = WorkCar(
        color="Gray",
        name="Ford",
    )

    police_car = PoliceCar(
        color="Blue",
        name="Hyundai",
    )

    car_list = [town_car, sport_car, work_car, police_car]

    for count in range(10):
        for car in car_list:
            car.go(randrange(0, 100))
            car.turn(directions[randrange(0, 3)])
            if randrange(0, 10) > 8:
                car.stop()

    for car in car_list:
        print(car.get_status())
