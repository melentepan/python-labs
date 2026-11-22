# Задание 3. На плоскости расположены три точки: A, B, C. Определить, какая из двух последних
# точек (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A.


def solve(ax, ay, bx, by, cx, cy):
    ab_squared = (bx - ax) ** 2 + (by - ay) ** 2
    ac_squared = (cx - ax) ** 2 + (cy - ay) ** 2
    if ab_squared < ac_squared:
        print('Ближе точка B:', bx, by)
        print('Расстояние:', ab_squared ** 0.5)
    elif ac_squared < ab_squared:
        print('Ближе точка C:', cx, cy)
        print('Расстояние:', ac_squared ** 0.5)
    else:
        print('Точки B и C равноудалены от A.')
        print('B:', bx, by)
        print('C:', cx, cy)
        print('Расстояние:', ab_squared ** 0.5)


# ax = float(input("Введите ax: "))
# ay = float(input("Введите ay: "))
# bx = float(input("Введите bx: "))
# by = float(input("Введите by: "))
# cx = float(input("Введите cx: "))
# cy = float(input("Введите cy: "))
# solve(ax, ay, bx, by, cx, cy)
