# Задание 9. Дана матрица размера M × N. Упорядочить ее строки так, чтобы их первые элементы
# образовывали возрастающую последовательность.


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(1, m):
        current_row = matrix[i]
        j = i - 1
        while j >= 0 and matrix[j][0] > current_row[0]:
            matrix[j + 1] = matrix[j]
            j -= 1
        matrix[j + 1] = current_row
    print('Упорядоченная матрица:')
    for row in matrix:
        print(*row)
