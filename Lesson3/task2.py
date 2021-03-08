"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы.

Например:
# >>> >>> num_translate_adv("One")
"Один"
# >>> num_translate_adv("two")
"два"
"""

dict_words = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(word):
    if word.istitle():
        word = word.lower()
        val_with_title = dict_words.get(word)
        val_with_title = val_with_title.title()
        print(val_with_title)

    else:
        return print(dict_words.get(word))


num_translate('Zero')
num_translate('one')
num_translate('Two')
num_translate('three')
num_translate('краказябра')
