"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
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

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён);
предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""

import os
from os import path
import shutil

PROJECT_ROOT = 'my_project'
template_dir = path.join(PROJECT_ROOT, 'templates')


def copy_dir(source, destination):
    for el in os.listdir(source):
        cur_dir = path.join(source, el)
        new_dir = path.join(destination, el)
        if path.isdir(cur_dir):
            if not path.isdir(new_dir):
                os.mkdir(new_dir)
            copy_dir(cur_dir, new_dir)
        elif path.isfile(cur_dir):
            if not path.isfile(new_dir):
                shutil.copy(cur_dir, new_dir)


for dirr in os.listdir(PROJECT_ROOT):
    if dirr.endswith('app'):
        if not path.isdir(template_dir):
            os.mkdir(template_dir)
        copy_dir(path.join(PROJECT_ROOT, dirr, 'templates'), template_dir)
