# Задание 1. Факториал числа: Напишите функцию, которая рекурсивно вычисляет факториал заданного
# числа n.


def factorial(n):
    if n < 0:
        raise ValueError('Факториал определен для неотрицательных чисел.')
    if n == 0:
        return 1
    return n * factorial(n - 1)

def solve(n):
    if n < 0:
        print('Число должно быть неотрицательным.')
    else:
        print('Факториал:', factorial(n))


# n = int(input("Введите n: "))
# solve(n)
