"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс «Клетка».

В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).

Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

Добавить к классу метод print(columns), распечатыващий на экране звездочки рядами по columns звездочек в одном ряду в
количестве равном числу ячеек клетки.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, если в клетке 12 ячеек, а запросили напечатать по 5 звездочек в ряду, то на экране должно быть:

*****
*****
**
"""


class OrganicCell(object):
    def __init__(self, sum_cell):
        self.sum_cell = sum_cell

    def __add__(self, other):
        result = self.sum_cell + other.sum_cell
        return OrganicCell(sum_cell=result)

    def __sub__(self, other):
        diff = self.sum_cell - other.sum_cell
        if diff > 0:
            return OrganicCell(sum_cell=diff)
        else:
            print("Клетки больше нет")

    def __mul__(self, other):
        multiply = self.sum_cell * other.sum_cell
        return OrganicCell(sum_cell=multiply)

    def __truediv__(self, other):
        div = self.sum_cell // other.sum_cell
        return OrganicCell(sum_cell=div)

    def print(self, columns):
        ful_cells = self.sum_cell // columns
        cells_remaining = self.sum_cell % columns
        result = '\n'.join(['*' * columns] * ful_cells) + '\n' + '*' * cells_remaining + '\n'
        return print(result)


if __name__ == '__main__':
    cell1 = OrganicCell(12)
    cell2 = OrganicCell(3)
    cell3 = cell1 + cell2

    cell1.print(5)
    cell2.print(2)
    cell3.print(7)
