"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""
# import requests
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# import requests
#
# r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
# print(r.text)

from requests import get
import xml.etree.ElementTree as ElT


def get_currency_rate(currency):
    """

    :param currency:
    :return:
    """
    currency = currency.upper()
    request = get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ElT.fromstring(request.text)
    for el in root:
        char_code = el.find('CharCode').text

        if char_code == currency:
            course = el.find('Value').text
            course = float(course.replace(',', '.'))
            return course


print(get_currency_rate('USD'))
print(get_currency_rate('EuR'))
print(get_currency_rate('111'))
