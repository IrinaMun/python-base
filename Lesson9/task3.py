"""
3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с учётом премии
get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position, вывести на экран имя
сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.
"""

# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
from pprint import pprint


class Employee:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Employee):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def get_position(self):
        return self.position


if __name__ == '__main__':
    position = Position(name='Jhon',
                        surname='Doe',
                        position='developer',
                        income={'wage': 60000,
                                'bonus': 30000})

    position2 = Position(name='Jane',
                         surname='Parker',
                         position='manager',
                         income={'wage': 40000,
                                 'bonus': 15000})

    print(f'Name of employee: {position.get_full_name()};\n'
          f'position: {position.get_position()};\n'
          f'income: {position.get_total_income()}.')
    print('\n******************************\n')
    print(f'Name of employee: {position2.get_full_name()};\n'
          f'position: {position2.get_position()};\n'
          f'income: {position2.get_total_income()}.')
