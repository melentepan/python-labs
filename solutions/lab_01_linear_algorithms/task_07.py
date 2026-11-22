# Задание 7. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.


def solve(a, b, c):
    ac = abs(c - a)
    bc = abs(c - b)
    print('Длина AC:', ac)
    print('Длина BC:', bc)
    print('Сумма длин:', ac + bc)


# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))
# solve(a, b, c)
