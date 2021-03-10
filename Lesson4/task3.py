"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.
"""

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


print(get_currency_rate('usd'))
print(get_currency_rate('Eur'))
print(get_currency_rate('2734jm'))
