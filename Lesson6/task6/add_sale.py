"""
script for data write
to terminal:
python lesson6\task6\add_sale.py 5978,5
python lesson6\task6\add_sale.py 8914,3
python lesson6\task6\add_sale.py 7879,1
python lesson6\task6\add_sale.py 1573,7
"""
import sys

FILE_NAME = '../bakery.csv'


def write_sum(value):
    with open(FILE_NAME, 'a+', encoding='utf-8') as f:
        f.seek(0)
        f.write(value + '\n')


if __name__ == '__main__':
    args = sys.argv[1:]
    for arg in args:
        try:
            # If not digit
            write_sum(arg.replace(',', '.'))
        except ValueError:
            continue
