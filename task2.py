# Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в
# файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.
import json


def write_order_to_json(filepath, **kwargs):
    with open(filepath, encoding='UTF-8') as json_file:
        data = json.load(json_file)

    data['orders'].append(kwargs)

    with open(filepath, 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    for_write = [
        {'item': 'TV',
         'quantity': 5,
         'price': 32000.00,
         'buyer': 'Все',
         'date': '26-12-2021'},
    ]

    for order in for_write:
        write_order_to_json('orders.json', **order)