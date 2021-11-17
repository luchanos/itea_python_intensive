"""
Домашнее задание:

Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
зарегистрируйте собственного бота через BotFather, а затем с использованием библиотеки telebot (PyTelegramBotAPI)
преобразуйте весь консольный функционал по взаимодействию с пользователем таким образом, чтобы все команды,
кроме останова программы (stop) можно было отправлять через Telegram.
"""

import json
from telebot import TeleBot

TOKEN = "2104221180:AAHg1uLK1NT5mN20Pas9FCiDjTprHH0Qua8"

bot = TeleBot(TOKEN)


def load_all_deals_from_file():
    """Функция для получения актуального списка дел из файла"""
    with open("my_tasks.json", "r") as tasks_json:
        notebook = json.load(tasks_json)
    return notebook


def get_all_notebook_str():
    notebook = load_all_deals_from_file()
    str_result = ""

    for deal_date in notebook:
        str_result += f"{deal_date}\n"
        num_deal = 0
        for deal in notebook[deal_date]:
            str_deal = f"{num_deal} {deal}"
            str_result += f"{str_deal}\n"
            num_deal += 1
        str_result += "\n"
    return str_result


@bot.message_handler(commands=["add_deal"])
def add_deal(message):
    """Добавление нового дела"""

    # выгружаем информацию о делах из принятого сообщения
    data_from_tg = message.text[10:].split(",")
    deal_date = data_from_tg[0]
    deal_description = data_from_tg[1]

    notebook = load_all_deals_from_file()

    if deal_date not in notebook:
        notebook[deal_date] = [deal_description, ]
    else:
        notebook[deal_date].append(deal_description)

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    show_all_deals_in_notebook(message)


@bot.message_handler(commands=["delete_all_deals_by_date"])
def delete_all_deals_by_date(message):
    """Удаление всех дел за определённую дату"""

    # получаем дату из принятого сообщения
    data_from_tg = message.text[26:].split()
    deal_date = data_from_tg[0]
    notebook = load_all_deals_from_file()

    notebook.pop(deal_date)

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    show_all_deals_in_notebook(message)


@bot.message_handler(commands=["delete_deal_by_date"])
def delete_deal_by_date(message):
    """Удаление одного дела за определённую дату"""

    # получаем дату из принятого сообщения
    data_from_tg = message.text[21:].split(",")
    deal_date = data_from_tg[0]
    num_deal = int(data_from_tg[1])

    notebook = load_all_deals_from_file()

    notebook[deal_date].pop(num_deal)

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    show_all_deals_in_notebook(message)


@bot.message_handler(commands=["show_all_deals_in_notebook"])
def show_all_deals_in_notebook(message):
    """Вывод полного списка дел на экран"""
    bot.reply_to(message, text=get_all_notebook_str())


bot.polling()
