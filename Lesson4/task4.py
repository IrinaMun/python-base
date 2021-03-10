"""
Задание 4. Модуль utils
Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:

если используется функция из 2-го задания:
USD 75.18
EUR 80.35
либо, если используется функция из 3-го задания
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""
import Lesson4.mymodule

print(Lesson4.mymodule.get_currency_rate('usd'))
print(Lesson4.mymodule.get_currency_rate('Eur'))
print(Lesson4.mymodule.get_currency_rate('2734jm'))
