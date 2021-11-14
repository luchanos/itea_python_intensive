from telebot import TeleBot
import json

TOKEN = "2104221180:AAHg1uLK1NT5mN20Pas9FCiDjTprHH0Qua8"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["add_product"])
def add_product(message):
    with open("my_shiny_json.json", "r") as json_file:
        all_products = json.load(json_file)
    product_data = message.text[13:].split(",")
    if len(product_data) < 3:
        bot.reply_to(message, text="Ошибка! Введите через запятую id, название продукта и его производителя!")
    else:
        new_product = {
                    "name": product_data[1],
                    "manufacturer": product_data[2]
                }
        all_products[product_data[0]] = new_product
        # записываем в json наш изменённый словарь
        with open("my_shiny_json.json", "w") as json_file:
            # делаем красивые отступы
            json.dump(all_products, json_file, indent=4, ensure_ascii=False)
        bot.reply_to(message, f"Добавлен новый продукт: {product_data}")


@bot.message_handler(commands=["get_by_id"])
def get_by_id(message):
    with open("my_shiny_json.json", "r") as json_file:
        all_products = json.load(json_file)
    product_id = message.text[10:].split()[0]
    if product_id not in all_products:
        bot.reply_to(message, text="Такого id нет!")
    else:
        bot.reply_to(message, text=str(all_products[product_id]))


bot.polling()
