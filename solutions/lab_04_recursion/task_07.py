# Задание 7. Разложение числа на сумму простых чисел: Напишите функцию, которая рекурсивно
# разлагает заданное число на сумму простых чисел.


def prime_sum(n):
    if n == 2 or n == 3:
        return [n]
    if n % 2 == 0:
        return [2] + prime_sum(n - 2)
    return [3] + prime_sum(n - 3)

def solve(n):
    if n < 2:
        print('Разложение на сумму простых чисел невозможно.')
    else:
        result = prime_sum(n)
        print(n, '=', end=' ')
        print(*result, sep=' + ')


# n = int(input("Введите n: "))
# solve(n)
