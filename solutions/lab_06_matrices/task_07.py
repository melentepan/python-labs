# Задание 7. Дана матрица размера M × N. Поменять местами столбцы, содержащие минимальный и
# максимальный элементы матрицы.


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    minimum = matrix[0][0]
    maximum = matrix[0][0]
    minimum_column = 0
    maximum_column = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                minimum_column = j
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
                maximum_column = j
    for row in matrix:
        row[minimum_column], row[maximum_column] = (row[maximum_column], row[minimum_column])
    print('Преобразованная матрица:')
    for row in matrix:
        print(*row)
