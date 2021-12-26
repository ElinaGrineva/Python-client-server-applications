import csv
import re


def get_data():
    data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    with open('info_1.txt') as file:
        formed = []
        sys_char = []
        for line in file:
            try:
                result = re.search(r'.*', line)
                grouping = result.group()
                list_with_spaces = grouping.split(':')
                for i in list_with_spaces:
                    i = i.strip()
                    formed.append(i)
            except:
                AttributeError
        count = 0
        for j in formed:
            count = count + 1
            if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                sys_char.append(formed[count])
        os_prod_list.append(sys_char[1])
        os_name_list.append(sys_char[0])
        os_code_list.append(sys_char[2])
        os_type_list.append(sys_char[3])

    with open('info_2.txt') as file:
        formed = []
        sys_char = []
        for line in file:
            try:
                result = re.search(r'.*', line)
                grouping = result.group()
                list_with_spaces = grouping.split(':')
                for i in list_with_spaces:
                    i = i.strip()
                    formed.append(i)
            except:
                AttributeError
        count = 0
        for j in formed:
            count = count + 1
            if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                sys_char.append(formed[count])
        os_prod_list.append(sys_char[1])
        os_name_list.append(sys_char[0])
        os_code_list.append(sys_char[2])
        os_type_list.append(sys_char[3])

    with open('info_3.txt') as file:
        formed = []
        sys_char = []
        for line in file:
            try:
                result = re.search(r'.*', line)
                grouping = result.group()
                list_with_spaces = grouping.split(':')
                for i in list_with_spaces:
                    i = i.strip()
                    formed.append(i)
            except:
                AttributeError
        count = 0
        for j in formed:
            count = count + 1
            if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                sys_char.append(formed[count])
        os_prod_list.append(sys_char[1])
        os_name_list.append(sys_char[0])
        os_code_list.append(sys_char[2])
        os_type_list.append(sys_char[3])
    data.append(os_prod_list)
    data.append(os_name_list)
    data.append(os_code_list)
    data.append(os_type_list)
    return data


def write_to_csv(csv_file):
    with open(csv_file, 'w') as writer:
        csv_writer = csv.writer(writer)
        for row in get_data():
            csv_writer.writerow(row)


write_to_csv('data.csv')
with open('data.csv') as f_n:
    print(f_n.read())
