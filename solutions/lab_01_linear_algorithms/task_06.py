# Задание 6. Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2)


def solve(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print('Расстояние между точками:', distance)


# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))
# solve(x1, y1, x2, y2)
