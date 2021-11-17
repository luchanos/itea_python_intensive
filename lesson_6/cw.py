"""
Домашнее задание:

Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
с помощью функции register_next_step_handler орагнизуйте каскадный опросник вашего
пользователя в рамках уже реализованных функций вашего бота.
"""

from telebot import TeleBot
import json

TOKEN = "2104221180:AAHg1uLK1NT5mN20Pas9FCiDjTprHH0Qua8"

bot = TeleBot(TOKEN)


def some_other_func(message):
    bot.reply_to(message, text="Сообщение из функции some_other_func")


@bot.message_handler(commands=["test"])
def some_func(message):
    bot.reply_to(message, text="Сообщение из функции some_func")


@bot.message_handler(commands=["get_by_id"])
def get_by_id(message):
    with open("my_shiny_json.json", "r") as json_file:
        all_products = json.load(json_file)
    product_id = message.text[10:].split()[0]
    if product_id not in all_products:
        bot.reply_to(message, text="Такого id нет!")
    else:
        bot.reply_to(message, text=str(all_products[product_id]))


def get_product_manufacturer(message, product_id, product_name):
    with open("my_shiny_json.json", "r") as json_file:
        all_products = json.load(json_file)

    product_manufacturer = message.text
    product_data = {
        "name": product_name,
        "manufacturer": product_manufacturer
    }
    all_products[product_id] = product_data
    bot.register_next_step_handler(message, product_id, product_name)

    with open("my_shiny_json.json", "w") as json_file:
        # делаем красивые отступы
        json.dump(all_products, json_file, indent=4, ensure_ascii=False)
    bot.reply_to(message, f"Добавлен новый продукт: {product_data}")


def get_product_name(message, product_id):
    product_name = message.text
    bot.reply_to(message, text="Введите производителя нового продукта: ")
    bot.register_next_step_handler(message, get_product_manufacturer, product_id, product_name)


def get_product_id(message):
    product_id = message.text
    bot.reply_to(message, text="Введите название нового продукта: ")
    bot.register_next_step_handler(message, get_product_name, product_id)


@bot.message_handler(commands=["add_product_new"])
def add_product_new(message):
    bot.reply_to(message, text="Введите id нового продукта:")
    bot.register_next_step_handler(message, get_product_id)


bot.polling()
