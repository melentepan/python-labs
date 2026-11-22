# Задание 4. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.


def solve(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    print('Сумма квадратов:', a_squared + b_squared)
    print('Разность квадратов:', a_squared - b_squared)
    print('Произведение квадратов:', a_squared * b_squared)
    print('Частное квадратов:', a_squared / b_squared)


# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# solve(a, b)
