"""
Домашнее задание:

Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
проведите рефакторинг кода и разбейте логически обособленные участки кода на функции и
предусмотрите обработку возможных возникающих исключений.
"""

# просим пользователя ввести 2 числа чтобы поделить одно на другое
# a = int(input("Введите делимое: "))
# b = int(input("введите делитель: "))
# try:
#     c = a / b
# except:  # перехватываем все виды исключений
#     print("Возникла ошибка!")


# давайте добавим словарь
# d = {
#     "key_1": "value_1",
#     "key_2": "value_2"
# }

# a = 1
# b = 0
#
# try:
#     print(d["key_3"])
#     c = a / b
# except (ZeroDivisionError, KeyError) as err:  # перехватываем определённые типы исключений
#     print("Возникла ошибка!", type(err), err)

def divisor(a, b):
    return a / b

# объявляем пустой словарь
all_products = {}
answer = ""


def get_data_from_user(enter_info_msg, err_info_msg):
    """Функция для запроса информации у пользователя"""
    while True:
        some_data = input(enter_info_msg)
        if product_id in all_products:
            print(err_info_msg)
            continue
        return some_data


while True:
    answer = input("Желаете ввести новый продукт? [add]\n"
                   "Желаете извлечь продукт по id? [get]\n"
                   "Остановить работу программы? [stop]: ")
    if answer == "stop":
        print("Программа завершается...")
        break
    elif answer == "get":
        product_id = input("Введите id продукта: ")
        try:
            print(all_products[product_id])
        except KeyError as err:
            print("Ошибка! Продукта с таким идентификатором нет!", type(err), err)
    else:

        # получаем id нового продукта
        while True:
            product_id = input("Введите id нового продукта: ")
            if product_id in all_products:
                print("Такой id уже есть в словаре! Введите другой!")
                continue
            break

        # запрашиваем название нового продукта
        product_name = get_data_from_user("Введите название нового продукта: ",
                                          "Название продукта не может быть пустой строкой! Введите другое название!")

        # запрашиваем производителя нового продукта
        product_manufacturer = get_data_from_user("Введите производителя нового продукта: ",
                                                  "Производитель продукта не может быть пустой строкой!"
                                                  " Введите другого производителя!")

        new_product = {
            "name": product_name,
            "manufacturer": product_manufacturer
        }
        all_products[product_id] = new_product

        print("Новый продукт добавлен! Теперь список продуктов выглядит вот так:\n\n")
        for el in all_products:
            print(el, ":", all_products[el])

print("Программа завершена!")
