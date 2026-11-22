# Задание 8. Дана матрица размера M × N (M и N — четные числа). Поменять местами левую верхнюю и
# правую нижнюю четверти матрицы


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    half_rows = m // 2
    half_columns = n // 2
    for i in range(half_rows):
        for j in range(half_columns):
            other_i = i + half_rows
            other_j = j + half_columns
            matrix[i][j], matrix[other_i][other_j] = (matrix[other_i][other_j], matrix[i][j])
    print('Преобразованная матрица:')
    for row in matrix:
        print(*row)


# m = int(input("Введите количество строк: "))
# n = int(input("Введите количество столбцов: "))
# matrix = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
#     matrix.append(row)
# solve(matrix)
