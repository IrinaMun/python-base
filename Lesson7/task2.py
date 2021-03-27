"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os
import yaml

scr_dir = os.path.dirname(__file__)


def make_from_parsed_data(folder, current_path=scr_dir):
    for key, value_list in folder.items():
        new_folder = os.path.join(current_path, key)
        if not os.path.isdir(new_folder):
            os.mkdir(new_folder)

        for value in value_list:
            if isinstance(value, str):
                new_file = os.path.join(new_folder, value)
                open(new_file, 'w').close()
            elif isinstance(value, dict):
                make_from_parsed_data(value, current_path=new_folder)


path = 'hierarchy.yml'
with open(path, 'r') as f:
    parsed_yaml = yaml.load(f, Loader=yaml.Loader)
    make_from_parsed_data(parsed_yaml)
