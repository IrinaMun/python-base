from pprint import pprint

from Lesson11.task4_5_6 import Warehouse, Printer, Scanner, Xerox
warehouse1 = Warehouse()
warehouse2 = Warehouse()

while True:
    choice = input('Какой товар добавить на склад?\n 1 - Принтер  2 - Сканер  3 - Ксерокс\n'
                   'Выбор позиции (для завершения введите "stop"):')
    if choice == "1":
        choice_equip = Printer(name="HP",
                               color="white",
                               print_type="laser")
    elif choice == "2":
        choice_equip = Scanner(name="HP",
                               color="white",
                               resolution="A4")
    elif choice == "3":
        choice_equip = Xerox(name="HP",
                             color="white",
                             speed=500)
    elif choice == 'stop':
        print('Список оргтехники')
        break

    else:
        print("Некорректные данные")
        continue

    while True:
        num_choice = input("Введите количество товара:")
        if num_choice.isdigit():
            num_choice = int(num_choice)
            break

        else:
            print("Некорректные данные")
            continue

    for i in range(num_choice):
        warehouse1.storage_office_equipment(choice_equip)

pprint(warehouse1.storage)
