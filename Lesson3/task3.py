"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

делаем список с именами
делаем пустой словарь
выгрызаем первую букву имен, делаем ее ключом
сравниваем первую букву имени и ключ, если идентичны, имя запихиваем в значение
"""

# for el in employees:
#     letter = el[0]
#     tmp_list = []
#     dict_employees[letter] = tmp_list
#     if letter == el[0]:
#         tmp_list.append(el)
#         print(tmp_list)

# print(dict_employees)

employees = ['Игорь', 'Виктор', 'Илья', 'Вольдемар', 'Никита', 'Ирина', 'Наталья', 'Владимир', 'Нина']


def thesaurus(*args):
    dict_employees = {}
    for el in args:
        key = el[0]
        if key not in dict_employees.keys():
            dict_employees[key] = []
        dict_employees[key].append(el)
    return dict_employees


print(thesaurus(*employees))
