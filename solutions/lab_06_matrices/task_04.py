# Задание 4. Дана матрица размера M × N. В каждом ее столбце найти количество элементов, больших
# среднего арифметического всех элементов этого столбца


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for j in range(n):
        total = 0.0
        for i in range(m):
            total += matrix[i][j]
        average = total / m
        count = 0
        for i in range(m):
            if matrix[i][j] > average:
                count += 1
        print(f'Столбец {j + 1}, количество элементов больше среднего:', count)


# m = int(input("Введите количество строк: "))
# n = int(input("Введите количество столбцов: "))
# matrix = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
#     matrix.append(row)
# solve(matrix)
