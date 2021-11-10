"""
- постановка проблемы (3 мин)
- понятие работы с файлами в Python (5 мин)
- обзор методов для работы с файлами: чтение, запись, дозапись (7 мин)
- обзор методов split и join (5 мин)
- написание скрипта для записи информации о продуктах в файл txt (10 мин)
"""
import json

# # запись
# with open("my_shiny_file.txt", "w") as file:
#     file.write("тестовые данные")
#
# # дозапись
# with open("my_shiny_file.txt", "a") as file:
#     file.write("тестовые данные")
#
# # чтение
# with open("my_shiny_file.txt", "r") as file:
#     print(file.read())

# краткий обзор методов split и join
# with open("products.txt", "r") as file:
#     for line in file:
#         print(line)
#         print(line[:-1].split(","))
#
# print(",".join(["3", "Творог", "Ромашка"]))

# вспомним наш словарь из первого урока
d_1 = {
    1: {
        "name": "orange",
        "manufacturer": "Romashka"
    },
    2: {
        "name": "orange",
        "manufacturer": "Solnyshko"
    },
    3: {
        "name": "pineapple",
        "manufacturer": "Zvezda"
    }
}

# настоящие программисты предпочитают json
# выгружаем данные из Python в json
# with open("my_shiny_json.json", "w") as json_file:
#     json.dump(d_1, json_file)

# загружаем данные в Python из json
# with open("my_shiny_json.json", "r") as json_file:
#     d = json.load(json_file)
#     print(type(d), d)

with open("my_tasks.json", "r") as my_json:
    some_dict = json.load(my_json)
    print(some_dict)
