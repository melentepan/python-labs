# Задание 3. Даны целые числа N (> 2), A и B. Сформировать и вывести целочисленный массив размера
# N, первый элемент которого равен A, второй равен B, а каждый последующий элемент равен сумме
# всех предыдущих


def solve(n, a, b):
    numbers = [a, b]
    total = a + b
    for i in range(2, n):
        numbers.append(total)
        total += numbers[-1]
    print('Массив:', *numbers)


# n = int(input("Введите n: "))
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# solve(n, a, b)
