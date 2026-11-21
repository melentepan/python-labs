# Задание 5. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.


def solve(a, b):
    a_absolute = abs(a)
    b_absolute = abs(b)
    print('Сумма модулей:', a_absolute + b_absolute)
    print('Разность модулей:', a_absolute - b_absolute)
    print('Произведение модулей:', a_absolute * b_absolute)
    print('Частное модулей:', a_absolute / b_absolute)
