"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class DivZero(Exception):
    pass


num1 = input("Введите число:")
num2 = input("Введите число:")
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise DivZero()
    result = num1 / num2
except ValueError:
    print("Вы ввели не число!")
except DivZero:
    print("Вы ввели 0!")
else:
    print(result)