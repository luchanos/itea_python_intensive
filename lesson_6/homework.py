"""
Домашнее задание:

Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
с помощью функции register_next_step_handler орагнизуйте каскадный опросник вашего
пользователя в рамках уже реализованных функций вашего бота.
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


def add_deal_action(message, deal_date):
    deal = message.text
    notebook = load_all_deals_from_file()
    if deal_date not in notebook:
        notebook[deal_date] = [deal, ]
    else:
        notebook[deal_date].append(deal)

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    bot.reply_to(message, text="Успешно!")


def get_date_deal(message):
    deal_date = message.text
    bot.reply_to(message, f"Введите новое дело на {deal_date}:")
    bot.register_next_step_handler(message, add_deal_action, deal_date)


@bot.message_handler(commands=["add_deal"])
def add_deal(message):
    bot.reply_to(message, text="Введите дату для нового дела:")
    bot.register_next_step_handler(message, get_date_deal)


def delete_all_deals(message):
    deal_date = message.text
    notebook = load_all_deals_from_file()
    notebook.pop(deal_date)

    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)

    bot.reply_to(message, text="Успешно!")


@bot.message_handler(commands=["delete_all_deals_by_date"])
def delete_all_deals_by_date(message):
    """Удаление всех дел за определённую дату"""
    bot.reply_to(message, text="Введите дату за которую хотите удалить все дела:")
    bot.register_next_step_handler(message, delete_all_deals)


def del_single_deal(message, deal_date, notebook):
    deal_num = int(message.text)
    notebook[deal_date].pop(deal_num)
    with open("my_tasks.json", "w", encoding="utf-8") as tasks_json:
        json.dump(notebook, tasks_json, indent=4, ensure_ascii=False)
    bot.reply_to(message, text="Успешно!")


def get_date_for_delete_single(message):
    """Удаление одного дела за определённую дату"""
    deal_date = message.text
    notebook = load_all_deals_from_file()
    deal_list = notebook[deal_date]
    deal_str = ""
    cnt = 0
    while cnt < len(deal_list):
        deal_str += f"{cnt} {deal_list[cnt]}\n"
        cnt += 1
    bot.reply_to(message, text=deal_str)
    bot.reply_to(message, text="Введите порядковый номер дела, которое желаете удалить:")
    bot.register_next_step_handler(message, del_single_deal, deal_date, notebook)


@bot.message_handler(commands=["delete_deal_by_date"])
def delete_deal_by_date(message):
    bot.reply_to(message, text="Введите дату за которую хотите удалить дело:")
    bot.register_next_step_handler(message, get_date_for_delete_single)


@bot.message_handler(commands=["show_all_deals_in_notebook"])
def show_all_deals_in_notebook(message):
    """Вывод полного списка дел на экран"""
    bot.reply_to(message, text=get_all_notebook_str())


bot.polling()
