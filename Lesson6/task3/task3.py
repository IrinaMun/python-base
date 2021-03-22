"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.

Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
запятая.

Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

Сохранить словарь в файл.

Проверить сохранённые данные.

Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.

Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи

1-й файл: ФИО через запятую users.csv
2-й файл: хобби hobby.csv
"""

import sys

unit = {}
key_list = []
value_list = []

with open('users.csv', 'r', encoding='Windows-1251') as users:
    for el in users:
        key_dict = el.strip().replace(",", " ")
        key_list.append(key_dict)

with open('hobby.csv', 'r', encoding='Windows-1251') as hobby:
    for el in hobby:
        value_dict = el.strip()
        value_list.append(value_dict)

with open('users_hobby.csv', 'w', encoding='Windows-1251') as users_hobby:
    el = len(key_list) - len(value_list)
    while len(key_list) != len(value_list):
        if el < 0:
            for element in range(0, abs(el)):
                sys.exit(1)
        elif el > 0:
            for element in range(0, el):
                value_list.append(None)
    else:
        for key, value in zip(key_list, value_list):
            unit[key] = [i for i in value.split(",") if i]
    print(unit, file=users_hobby)
