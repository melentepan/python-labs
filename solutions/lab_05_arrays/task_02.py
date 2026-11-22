# Задание 2. Дано целое число N (> 1), а также первый член A и знаменатель D геометрической
# прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов данной
# прогрессии: A, A·D, A·D^2 , A·D^3 , . . .


def solve(n, a, d):
    numbers = []
    term = a
    for i in range(n):
        numbers.append(term)
        term *= d
    print('Массив:', *numbers)


# n = int(input("Введите n: "))
# a = float(input("Введите a: "))
# d = float(input("Введите d: "))
# solve(n, a, d)
