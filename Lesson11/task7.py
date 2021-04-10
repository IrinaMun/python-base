"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        else:
            return ComplexNumber(self.a + other, self.b)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a * other.a - (self.b * other.b), self.b * other.a)
        else:
            return ComplexNumber(self.a * other, self.b * other)

    def __str__(self):
        return f'{self.a} + {self.b}i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 + 123)
print(z_1 * z_2)