# Задание 4. Дан массив A размера N. Вывести его элементы в следующем порядке: A1, AN , A2, AN−1,
# A3, AN−2,


def solve(numbers):
    n = len(numbers)
    result = []
    left = 0
    right = n - 1
    while left <= right:
        result.append(numbers[left])
        if left != right:
            result.append(numbers[right])
        left += 1
        right -= 1
    print('Элементы в заданном порядке:', *result)
