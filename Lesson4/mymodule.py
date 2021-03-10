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
