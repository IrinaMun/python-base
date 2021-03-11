"""
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""
from sys import argv
from requests import get
import xml.etree.ElementTree as ElT
from decimal import Decimal
import datetime


def get_currency_rate(currency):
    """
    Функция, возвращающая дату и курс заданной валюты по отношению к рублю на текущий момент.

    :param currency: код валюты
    :return: tuple из кода валюты, курса валюты по отношению к рублю (Decimal) и текущей даты
    """
    currency = currency.upper()
    request = get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ElT.fromstring(request.text)
    date_obj = datetime.datetime.strptime(root.attrib['Date'], '%d.%m.%Y').date()
    for el in root:
        char_code = el.find('CharCode').text
        if char_code == currency:
            course = el.find('Value').text
            course = Decimal(course.replace(",", "."))
            return currency, course, f'{date_obj}'


# for el in argv[1:]:
#     print(get_currency_rate(el))

[print(get_currency_rate(el)) for el in argv[1:]] # компрехенция
