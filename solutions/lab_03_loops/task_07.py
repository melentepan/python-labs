# Задание 7. Даны положительные числа A и B (A > B). На отрезке длины A размещено максимально
# возможное количество отрезков длины B (без наложений). Не используя операции умножения и
# деления, найти длину незанятой части отрезка A.


def decimal_places(value):
    mantissa, _, exponent = str(value).partition('e')
    digits = len(mantissa.partition('.')[2])
    if exponent:
        digits -= int(exponent)
    return max(0, digits)


def solve(a, b):
    digits = max(decimal_places(a), decimal_places(b))
    remainder = a
    while remainder >= b:
        remainder = round(remainder - b, digits)
    print('Длина незанятой части:', remainder)


# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# solve(a, b)
