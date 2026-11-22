# Задание 10. Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали,
# параллельной главной (начиная с одноэлементной диагонали).


def solve(matrix):
    m = len(matrix)
    sums = []
    for offset in range(m - 1, -m, -1):
        total = 0.0
        for i in range(m):
            j = i + offset
            if 0 <= j < m:
                total += matrix[i][j]
        sums.append(total)
    print('Суммы диагоналей:', *sums)


# m = int(input("Введите количество строк: "))
# n = m
# matrix = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
#     matrix.append(row)
# solve(matrix)
