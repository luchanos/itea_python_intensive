print("Вас приветствует программа органайзер!")

notebook = {}

while True:
    answer = input("Добавить новое дело [add]\n"
                   "Удалить все дела за определённую дату [delete_all]:\n"
                   "Удалить определённое дело за определённую дату [delete_one]:\n"
                   "Завершить работу программы [stop]: ")

    # добавление нового дела
    if answer == "add":
        deal_date = input("Введите дату: ")
        deal_description = input("Введите дело, которое нужно не забыть: ")

        if deal_date not in notebook:
            notebook[deal_date] = [deal_description, ]
        else:
            notebook[deal_date].append(deal_description)

    # удаление всех дел за определённую дату
    elif answer == "delete_all":
        deal_date = input("Введите дату: ")
        notebook.pop(deal_date)

    # удаление одного дела за определённую дату
    elif answer == "delete_one":
        deal_date = input("Введите дату: ")
        num_deal = 0
        for deal in notebook[deal_date]:
            print(num_deal, deal)
            num_deal += 1
        num_for_deleteng = int(input(f"Введите номер дела за {deal_date} которое нужно удалить: "))
        notebook[deal_date].pop(num_for_deleteng)

    # завершение работы программы
    elif answer == "stop":
        print("Программа завершает работу...")
        break

    # вывод списка дел на экран
    for deal_date in notebook:
        print(deal_date)
        num_deal = 0
        for deal in notebook[deal_date]:
            print(num_deal, deal)
            num_deal += 1
        print()  # добавление пустой строки в вывод консоли

print("Программа завершила свою работу!")
