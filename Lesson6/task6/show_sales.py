"""
to terminal: python lesson6\task6\ show_sales.py
"""
from sys import argv
from add_sale import FILE_NAME


def show_opp(slice_beg=None, slice_end=None):
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        data = f.readlines()
    data = [float(i.replace(',', '.')) for i in data[slice_beg:slice_end]]
    print(data)


if __name__ == '__main__':
    args = argv[1:]
    show_opp(*[int(i) for i in args])
