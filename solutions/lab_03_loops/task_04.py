# Задание 4. Дано вещественное число A и целое число N (> 0). Используя один цикл, найти сумму 1 +
# A + A^2 + A^3 + . . . + A^N


def solve(a, n):
    power = 1
    total = 1
    for i in range(1, n + 1):
        power *= a
        total += power
    print('Сумма:', total)


# a = float(input("Введите a: "))
# n = int(input("Введите n: "))
# solve(a, n)
