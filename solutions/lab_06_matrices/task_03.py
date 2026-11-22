# Задание 3. Дана матрица размера M × N. Найти номер ее столбца с наименьшим произведением
# элементов и вывести данный номер, а также значение наименьшего произведения.


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    minimum_product = 1.0
    for i in range(m):
        minimum_product *= matrix[i][0]
    column_number = 1
    for j in range(1, n):
        product = 1.0
        for i in range(m):
            product *= matrix[i][j]
        if product < minimum_product:
            minimum_product = product
            column_number = j + 1
    print('Номер столбца:', column_number)
    print('Наименьшее произведение:', minimum_product)


# m = int(input("Введите количество строк: "))
# n = int(input("Введите количество столбцов: "))
# matrix = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
#     matrix.append(row)
# solve(matrix)
