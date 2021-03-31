"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube()
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:

>>> a = calc_cube()
calc_cube(5: <class 'int'>)
"""

def type_logger(func):
    def wrapper(*args):
        for i in args:
            print(f"{i}: {type(i)}")
        ret = func(*args)
        return ret

    return wrapper


@type_logger
def calc_sum(a, b):
    return a + b


@type_logger
def calc_cube(x):
    return x ** 3


calc_sum(10, 20)

calc_cube(10)
