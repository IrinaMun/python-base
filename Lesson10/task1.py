"""
1. Реализовать класс Matrix (матрица).
Конструктор класса __init__() должен принимать список списков чисел для задания превоначального состояния матрицы.
Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
В методе __init__() надо проверить корректность передаваемых данных - все списки должны быть одинаковой длины.
В случае расхождения выбрасывать исключение ValueError с соответствующим описанием.
Добавить метод __add__() сложения двух матриц. Складывать можно матрицы одинаковой размерности.
В случае, когда пользователь пытается сложить матрицы разных размеров выбросить исключение ValueError.
В результате сложения двух матриц должна образоваться новая матрица размером N x M, где каждый элемент в ячейке i,j
образован сложением значений из соответствующих ячеек исходных матриц.
Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6", отводя под числа по три разряда, чтобы для
небольших чисел матрица выглядела как таблица.
Создать три матрицы (две одинаковые по размеру и одну с другим размером).
Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат сложения.
"""

from copy import copy


class Matrix(object):
    def __init__(self, matrix):
        if isinstance(matrix, list):
            for index, el in enumerate(matrix):
                if len(el) != len(matrix[index - 1]):
                    raise ValueError("Длина вложенных списков не совпадает!")

        self.matrix = matrix

    def __str__(self) -> str:
        return str(self.matrix)

    def __repr__(self) -> str:
        return "\n".join([str(i) for i in self.matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise Exception("слагаемое не экземпляр класса Matrix!")
        if self.shape != other.shape:
            raise ValueError ("Форма матриц разная!")
        new_matrix = copy(self)
        for x, row in enumerate(other.matrix):
            for y, el in enumerate(row):
                new_matrix.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return new_matrix

    @property
    def shape(self):
        row = len(self.matrix)
        column = len(self.matrix[0])
        return row, column


if __name__ == '__main__':
    matrix1 = Matrix(matrix=[[1, 4, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix(matrix=[[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(repr(matrix1 + matrix2))
