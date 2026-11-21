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
