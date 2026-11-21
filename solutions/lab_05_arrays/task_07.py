# Задание 7. Дан целочисленный массив размера N, не содержащий одинаковых чисел. Проверить,
# образуют ли его элементы арифметическую прогрессию. Если образуют, то вывести разность
# прогрессии, если нет — вывести 0.


def solve(numbers):
    n = len(numbers)
    difference = numbers[1] - numbers[0]
    for i in range(2, n):
        if numbers[i] - numbers[i - 1] != difference:
            difference = 0
            break
    print('Разность прогрессии или 0:', difference)
