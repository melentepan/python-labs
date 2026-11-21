# Задание 5. Дана целочисленная матрица размера M × N. Найти номер первого из ее столбцов,
# содержащих только нечетные числа. Если таких столбцов нет, то вывести 0.


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    column_number = 0
    for j in range(n):
        only_odd = True
        for i in range(m):
            if matrix[i][j] % 2 == 0:
                only_odd = False
                break
        if only_odd:
            column_number = j + 1
            break
    print('Номер первого столбца только с нечетными числами:', column_number)
