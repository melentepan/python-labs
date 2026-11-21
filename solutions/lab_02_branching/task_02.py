# Задание 2. Даны три числа. Найти сумму двух наибольших из них


def solve(a, b, c):
    if a <= b and a <= c:
        total = b + c
    elif b <= a and b <= c:
        total = a + c
    else:
        total = a + b
    print('Сумма двух наибольших чисел:', total)
