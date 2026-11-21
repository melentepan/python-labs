# Задание 5. Дан массив A размера N. Вывести вначале его элементы с нечетными номерами в порядке
# возрастания номеров, а затем — элементы с четными номерами в порядке убывания номеров


def solve(numbers):
    n = len(numbers)
    result = []
    for i in range(0, n, 2):
        result.append(numbers[i])
    last_even_number = n - n % 2
    for i in range(last_even_number - 1, 0, -2):
        result.append(numbers[i])
    print('Элементы в заданном порядке:', *result)
