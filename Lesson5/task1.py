"""
# Задание 1. Функция-генератор rand_nums
# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#
# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
# 11
# >>> next(rand15) # 2-й вызов
# 38
# ...
# >>> next(rand15) # 15-й вызов
# 7
# >>> next(rand15) # 16-й вызов
# ...StopIteration...
"""

from random import randint


def rand_nums(limit):
    counter = 1
    while counter <= limit:
        rand_number = randint(1, 100)
        yield rand_number
        counter += 1


rand = rand_nums(3)
try:
    print(next(rand))
    print(next(rand))
    print(next(rand))
    print(next(rand))
except StopIteration:
    print('...StopIteration...')
