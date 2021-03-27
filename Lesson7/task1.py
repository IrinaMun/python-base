"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os

hierarchy = {
    'my_project': {
        'settings': '',
        'mainapp': '',
        'admin': '',
        'authapp': ''
    }
}


def make_hierarchy(dir_dict, root_dir):
    for key, value in dir_dict.items():
        if not os.path.isdir(os.path.join(root_dir, key)):
            os.makedirs(os.path.join(root_dir, key))
        if isinstance(value, dict):
            make_hierarchy(value, os.path.join(root_dir, key))


make_hierarchy(hierarchy, os.getcwd())
