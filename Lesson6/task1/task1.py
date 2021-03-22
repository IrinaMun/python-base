"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_adr>, <request_type>, <requested_resource>).

Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    result = []
    for line in f:
        a = line.split()
        el0 = (a[0], a[5], a[6])
        result.append(str(el0))
    with open('new_file.txt', 'w', encoding='utf-8') as new:
        new.write("[\n" + ",\n".join(result) + "\n]")
