"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков
(по одному слову из каждого списка):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_of_jokes, word_repetition=True):
    """
    Функция генерирует шутки из заданных списков,
    случайно выбирая по одному элементу из каждого списка и возвращает новый список из этих элементов
    :param number_of_jokes: количество шуток на выходе
    :param word_repetition: хрень с которой надо разобраться
    :return: список из шуток

    """

    result_jokes = []
    if not word_repetition:
        min_len = min(len(nouns),
                      len(adverbs),
                      len(adjectives))
        if min_len < number_of_jokes:
            return f"Максимальное количество шуток {min_len}. Нельзя так много шутить."

    while number_of_jokes:
        joke = [choice(nouns), choice(adverbs), choice(adjectives)]
        if not word_repetition:
            nouns.remove(joke[0])
            adverbs.remove(joke[1])
            adjectives.remove(joke[2])
        joke = " ".join(joke)
        result_jokes.append(joke)
        number_of_jokes -= 1

    return result_jokes


print(get_jokes(10, word_repetition=True))
print(get_jokes(10, word_repetition=False))

employees = ['Игорь Чеботкевич',
             'Виктор Чеботкевич',
             'Илья Лавров',
             'Вольдемар Лангерн',
             'Никита Лавров',
             'Ирина Мун',
             'Наталья Миронова',
             'Владимир Черепков',
             'Нина Макарова']


def thesaurus_adv(*args):
    dict_employees = {}
    for el in args:
        el = el.split()
        key = el[1]
        key2 = key[0]
        if key2 not in dict_employees.keys():
            dict_employees[key2] = []
        dict_employees[key2].append(' '.join(el))
    return dict_employees


print(thesaurus_adv(*employees))
