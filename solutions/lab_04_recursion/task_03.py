# Задание 3. Возведение в степень: Напишите функцию, которая рекурсивно возводит число x в степень
# n.


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

def solve(x, n):
    if x == 0 and n < 0:
        print('Ноль нельзя возвести в отрицательную степень.')
    else:
        print('Результат:', power(x, n))
