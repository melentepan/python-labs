# Задание 8. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B.
# Найти произведение длин отрезков AC и BC


def solve(a, b, c):
    ac = abs(c - a)
    bc = abs(c - b)
    print('Произведение длин AC и BC:', ac * bc)


# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))
# solve(a, b, c)
