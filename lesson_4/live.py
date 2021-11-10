# это называется импорт пакетов или модулей. импорт в подавляющих случаях указывается
# в начале модуля
import json  # модуль для работы с json

# открытие файла
# json_file = open("my_shiny_json.json", "r")
# print(json_file, f"файл закрыт? - {json_file.closed}")
# data_from_json = json.load(json_file)
# print(data_from_json, type(data_from_json))
# print(json_file, f"файл закрыт? - {json_file.closed}")
# # закрытие файла
# json_file.close()
# print(json_file, f"файл закрыт? - {json_file.closed}")

some_dict = {"это": "просто словарь"}
json_file = open("my_shiny_json.json", "w", encoding="utf-8")
json.dump(some_dict, json_file)  # + indent=4, ensure_ascii=False
json_file.close()

# # чтобы автоматизировать операцию закрытия можно использовать контекстный менеджер
# with open("my_shiny_json.json", "r") as my_file_object:
#     print(json_file, f"файл закрыт? - {json_file.closed}")
#     data_from_json = json.load(my_file_object)
#     print(data_from_json, type(data_from_json))
#     print(json_file, f"файл закрыт? - {json_file.closed}")
# print(json_file, f"файл закрыт? - {json_file.closed}")
# print("работа завершена")

# читаем базу с продуктами из файла
# with open("my_shiny_json.json", "r") as json_file:
#     all_products = json.load(json_file)

# answer = ""
#
#
# def get_data_from_user(enter_info_msg, err_info_msg):
#     """Функция для запроса информации у пользователя"""
#     while True:
#         some_data = input(enter_info_msg)
#         if some_data == "":
#             print(err_info_msg)
#             continue
#         return some_data
#
#
# while True:
#     answer = input("Желаете ввести новый продукт? [add]\n"
#                    "Желаете извлечь продукт по id? [get]\n"
#                    "Остановить работу программы? [stop]: ")
#     if answer == "stop":
#         print("Программа завершается...")
#         break
#     elif answer == "get":
#         product_id = input("Введите id продукта: ")
#         try:
#             print(all_products[product_id])
#         except KeyError as err:
#             print("Ошибка! Продукта с таким идентификатором нет!", type(err), err)
#
#     elif answer == "add":
#         # получаем id нового продукта
#         while True:
#             product_id = input("Введите id нового продукта: ")
#             if product_id in all_products:
#                 print("Такой id уже есть в словаре! Введите другой!")
#                 continue
#             break
#
#         # запрашиваем название нового продукта
#         product_name = get_data_from_user("Введите название нового продукта: ",
#                                           "Название продукта не может быть пустой строкой! Введите другое название!")
#
#         # запрашиваем производителя нового продукта
#         product_manufacturer = get_data_from_user("Введите производителя нового продукта: ",
#                                                   "Производитель продукта не может быть пустой строкой!"
#                                                   " Введите другого производителя!")
#
#         new_product = {
#             "name": product_name,
#             "manufacturer": product_manufacturer
#         }
#         all_products[product_id] = new_product
#
#         print("Новый продукт добавлен! Теперь список продуктов выглядит вот так:\n\n")
#         for el in all_products:
#             print(el, ":", all_products[el])
#
#         # записываем в json наш изменённый словарь
#         with open("my_shiny_json.json", "w") as json_file:
#             # делаем красивые отступы
#             json.dump(all_products, json_file, indent=4, ensure_ascii=False)
#
# print("Программа завершена!")
