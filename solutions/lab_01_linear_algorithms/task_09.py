# Задание 9. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2).
# Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного
# прямоугольника.


def solve(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    print('Периметр:', perimeter)
    print('Площадь:', area)


# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))
# solve(x1, y1, x2, y2)
