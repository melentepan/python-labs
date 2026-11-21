# Задание 6. Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и
# максимальный элемент в каждой строке.


def solve(matrix):
    n = len(matrix[0])
    for row in matrix:
        minimum_index = 0
        maximum_index = 0
        for j in range(1, n):
            if row[j] < row[minimum_index]:
                minimum_index = j
            if row[j] > row[maximum_index]:
                maximum_index = j
        row[minimum_index], row[maximum_index] = (row[maximum_index], row[minimum_index])
    print('Преобразованная матрица:')
    for row in matrix:
        print(*row)
