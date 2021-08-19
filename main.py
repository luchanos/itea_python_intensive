"""
Характеристики дел на день:
1. Дата (или дата и время)
2. Описание дела
3. Уровень важности от 0 до 100 баллов

Пример:
Навестить маму:

01-09-2021 Навестить любимую маму 100
"""

# deal = ["01-09-2021", "Навестить любимую маму", 100]
# print(deal[0])

deal_1 = {
    "date": "01-09-2021",
    "description": "Навестить любимую маму",
    "importance": 100
}

deal_2 = {
    "date": "02-09-2021",
    "description": "Сходить в кино",
    "importance": 50
}

deal_list = []

# for el in deal_list:
#     print(el)

# some_data = input("Введите данные: ")
# print("Вы ввели:", some_data)

print("Приветствую!")

while True:
    deal_dict = dict()
    user_answer = input("Желаете ли завести новое дело в ежедневнике? [y/n]")
    if user_answer.lower() not in {"y", "n"}:
        print("Я вас не понимаю, повторите ввод!")
    else:
        if user_answer == "y":
            deal_dict["date"] = input("Введите дату: ")
            deal_dict["description"] = input("Введите описание: ")
            deal_dict["importance"] = int(input("Введите важность от 0 до 100: "))
            print("Вы ввели дело:", deal_dict)
            deal_list.append(deal_dict)
            for el in deal_list:
                print(el)
        else:
            break
