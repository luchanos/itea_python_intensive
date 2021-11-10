"""
Домашнее задание:

Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
добавьте подключение к json-файлу, который бы являлся хранилищем информации о делах
(по сути аналогом базы данных). Реализуйте вывод списка дел за выбранную дату на экран.
Дату запрашивать у пользователя через консоль.
"""
import json

print("Вас приветствует программа органайзер!")


def add_deal(notebook):
    """Добавление нового дела"""
    deal_date = input("Введите дату: ")
    deal_description = input("Введите дело, которое нужно не забыть: ")

    if deal_date not in notebook:
        notebook[deal_date] = [deal_description, ]
    else:
        notebook[deal_date].append(deal_description)
    # или делать return notebook


def delete_all_deals_by_date(notebook):
    """Удаление всех дел за определённую дату"""
    deal_date = input("Введите дату: ")
    notebook.pop(deal_date)
    # или делать return notebook


def delete_deal_by_date(notebook):
    """Удаление одного дела за определённую дату"""
    deal_date = input("Введите дату: ")
    num_deal = 0
    for deal in notebook[deal_date]:
        print(num_deal, deal)
        num_deal += 1
    num_for_deleteng = int(input(f"Введите номер дела за {deal_date} которое нужно удалить: "))
    notebook[deal_date].pop(num_for_deleteng)
    # или делать return notebook


def show_all_deals_in_notebook(notebook):
    """Вывод полного списка дел на экран"""
    for deal_date in notebook:
        print(deal_date)
        num_deal = 0
        for deal in notebook[deal_date]:
            print(num_deal, deal)
            num_deal += 1
        print()  # добавление пустой строки в вывод консоли


# прогружаем дела из json-файла
with open("my_tasks.json", "r") as tasks_json:
    notebook = json.load(tasks_json)

while True:
    answer = input("Добавить новое дело [add]\n"
                   "Удалить все дела за определённую дату [delete_all]:\n"
                   "Удалить определённое дело за определённую дату [delete_one]:\n"
                   "Вывести все дела на экран [show_all]:\n"
                   "Завершить работу программы [stop]: ")

    if answer == "add":
        add_deal(notebook)
    elif answer == "delete_all":
        try:
            delete_all_deals_by_date(notebook)
        except KeyError as err:
            print("Ошибка! Вы ввели некорректную дату!", type(err), err)
    elif answer == "delete_one":
        try:
            delete_deal_by_date(notebook)
        except KeyError as err:
            print("Ошибка! Вы ввели некорректную дату!", type(err), err)
    elif answer == "show_all":
        show_all_deals_in_notebook(notebook)

    # завершение работы программы
    elif answer == "stop":
        print("Программа завершает работу...")
        break

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    if answer != "show_all":
        show_all_deals_in_notebook(notebook)

print("Программа завершила свою работу!")
