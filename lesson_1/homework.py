"""Разработать структуру для хранения информации для отображения списка дел
в привязке к датам. Учитывайте, что к одной дате могут относиться сразу несколько дел.
Попробуйте поиграться с этим списком - программно добавьте новое дело или удалите его.
Программно попробуйте удалить все дела за выбранную дату.
"""

# пример переменной с датой
date_template = '01-01-2021'

# пример переменной с "делом"
deal_template = {
    "description": "call to mom",
    "severity": "high",
    "labor_intensity": 3
}

# пример структуры для нашего ежедневника
notebook = {
    '01-01-2021': [
        {
            "description": "call to mom",
            "severity": "high",
            "labor_intensity": 2
        },
        {
            "description": "buy bread",
            "severity": "low",
            "labor_intensity": 4
        },
        {
            "description": "make homework",
            "severity": "high",
            "labor_intensity": 10
        }
    ],
    '02-03-2021': [
        {
            "description": "get some training",
            "severity": "medium",
            "labor_intensity": 7
        },
        {
            "description": "visit theatre",
            "severity": "medium",
            "labor_intensity": 5
        }
    ],
    '11-05-2020': [
        {
            "description": "repair the car in service",
            "severity": "high",
            "labor_intensity": 20
        },
        {
            "description": "make a cake",
            "severity": "low",
            "labor_intensity": 2
        },
        {
            "description": "create the video",
            "severity": "high",
            "labor_intensity": 10
        },
        {
            "description": "book the hotel for vacations",
            "severity": "high",
            "labor_intensity": 9
        }
    ]
}

# вывести полный список дел
print(notebook)

# вывести список дел за 01-01-2021
# print(notebook['01-01-2021'])

# вывести первое дело в списке за 01-01-2021
# print(notebook['01-01-2021'][0])

# вывести описание первого дела в списке за 01-01-2021
# print(notebook['01-01-2021'][0]['description'])

new_date = '03-08-2021'
new_deal = {
            "description": "buy oranges",
            "severity": "low",
            "labor_intensity": 4
           }

deal_list = [
    new_deal,
]

# привязываем список с делами по ключу даты
# notebook[new_date] = deal_list

# вывести список дел за 03-08-2021
# print(notebook['03-08-2021'])

# добавляем ещё пару дел
new_deal_2 = {
              "description": "watch tutorial",
              "severity": "high",
              "labor_intensity": 3
             }

new_deal_3 = {
              "description": "visit doctor",
              "severity": "high",
              "labor_intensity": 5
             }

# добавляем ещё два дела за 03-08-2021
# notebook[new_date].append(new_deal_2)
# notebook[new_date].append(new_deal_3)

# вывести список дел за 03-08-2021
# print(notebook['03-08-2021'])

# удаляем дело
# notebook[new_date].pop(0)

# вывести список дел за 03-08-2021
# print(notebook['03-08-2021'])

# удалить все дела за выбранную дату
# notebook.pop('03-08-2021')

# вывести список дел за 03-08-2021
# print(notebook)
