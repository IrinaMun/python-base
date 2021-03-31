# """
# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError.

# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)

# ValueError: wrong email: someone@geekbrainsru

# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
# """

import re


def email_parse(*args):
    my_str = str(args)
    parsed = re.findall(r'[a-zA-Z0-9.+-]+', my_str)
    parsed_1 = re.findall(r'[a-zA-Z0-9.+-]+\.[a-zA-Z0-9.+-]+', my_str)
    if not parsed_1:
        raise ValueError(f'wrong email: {parsed[1]}')
    return dict(zip(['username', 'domain'], parsed))


print(email_parse('someone@geekbrains.ru'))
email_parse('someone@geekbrainsru')
