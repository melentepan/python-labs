# Задание 1. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, . . . , 1 кг
# конфет.


def solve(price):
    for i in range(1, 11):
        weight = i / 10
        cost = price * weight
        print(f'{weight:.1f} кг - {cost:.2f} руб.')
