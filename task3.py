# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
# файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число
# с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# # Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также
# установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


def yaml_download(file_name):
    for_write = {5: [1, 3, 5], 2: 23, 3: {3: '1€', '13': '2€'}}

    with open(file_name, 'w', encoding='UTF-8') as file:
        yaml.dump(for_write, file, default_flow_style=False, allow_unicode=True)

    with open(file_name, encoding='UTF-8') as file:
        for_read = yaml.load(file, yaml.Loader)
        print(for_read)


yaml_download('my_yaml.yaml')