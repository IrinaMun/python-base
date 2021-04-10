"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import datetime


class Date(object):
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def num_date(cls, int_date):
        int_date = str(int_date)
        return [int(i) for i in int_date.split("-")]

    @staticmethod
    def val_date(day, month, year):
        if day > 31 or month > 12 or year < 0:
            print("Incorrect date")
            return False
        else:
            return True


if __name__ == '__main__':
    date = Date.num_date(int_date=datetime.date.today())
    d = datetime.date.today()
    valid_date = Date.val_date(day=d.day,
                               month=d.month,
                               year=d.year)
    print(date)
    print(valid_date)