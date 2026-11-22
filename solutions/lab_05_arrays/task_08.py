# Задание 8. Дан массив A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6,


def solve(numbers):
    n = len(numbers)
    minimum = numbers[1]
    for i in range(3, n, 2):
        if numbers[i] < minimum:
            minimum = numbers[i]
    print('Минимум среди элементов с четными номерами:', minimum)


# numbers = list(map(float, input('Введите числа через пробел: ').split()))
# solve(numbers)
