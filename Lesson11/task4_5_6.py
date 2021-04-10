"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipment(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.class_name = None


class Warehouse(object):
    def __init__(self):
        self.storage = {}

    def storage_office_equipment(self, equipment: OfficeEquipment):
        if not self.storage.get(equipment.class_name):
            self.storage[equipment.class_name] = [equipment]
        else:
            self.storage[equipment.class_name].append(equipment)

    def remove_equipment(self, equipment: OfficeEquipment):
        if equipment in self.storage.get(equipment.class_name, []):
            shelf = self.storage[equipment.class_name]
            equip_index = shelf.index(equipment)
            res_equipment = shelf.pop(equip_index)
            return res_equipment
        else:
            print("Такого оборудования нет на складе")

    def transfer_equipment(self, equipment: OfficeEquipment, other_warehouse):
        trans_equip = self.remove_equipment(equipment)
        if trans_equip:
            other_warehouse.storage_office_equipment(trans_equip)


class Printer(OfficeEquipment):
    def __init__(self, name, color, print_type):
        super().__init__(name, color)
        self.print_type = print_type
        self.class_name = 'Printer'

    def __repr__(self):
        return f'({self.class_name}: name: {self.name}, color: {self.color}, type: {self.print_type})'


class Scanner(OfficeEquipment):
    def __init__(self, name, color, resolution):
        super().__init__(name, color)
        self.resolution = resolution
        self.class_name = 'Scanner'

    def __repr__(self):
        return f'({self.class_name}: name: {self.name}, color: {self.color}, resolution: {self.resolution})'


class Xerox(OfficeEquipment):
    def __init__(self, name, color, speed):
        super().__init__(name, color)
        self.speed = speed
        self.class_name = 'Xerox'

    def __repr__(self):
        return f'({self.class_name}: name: {self.name}, color: {self.color}, speed: {self.speed})'
