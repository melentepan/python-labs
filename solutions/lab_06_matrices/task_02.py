# Задание 2. Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). Найти сумму и произведение
# элементов K-й строки данной матрицы.


def solve(matrix, k):
    n = len(matrix[0])
    total = 0.0
    product = 1.0
    for value in matrix[k - 1]:
        total += value
        product *= value
    print('Сумма:', total)
    print('Произведение:', product)


# m = int(input("Введите количество строк: "))
# n = int(input("Введите количество столбцов: "))
# matrix = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
#     matrix.append(row)
# k = int(input("Введите k: "))
# solve(matrix, k)
