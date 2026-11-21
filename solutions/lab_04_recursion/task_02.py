# Задание 2. Числа Фибоначчи: Напишите функцию, которая рекурсивно вычисляет n-ое число Фибоначчи.


def fibonacci(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def solve(n):
    if n < 0:
        print('Номер должен быть неотрицательным.')
    else:
        print('Число Фибоначчи:', fibonacci(n))
