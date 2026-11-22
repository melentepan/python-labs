# Задание 9. Дан массив размера N. Найти номер его последнего локального максимума (локальный
# максимум — это элемент, который больше любого из своих соседей).


def solve(numbers):
    n = len(numbers)
    last_maximum = 0
    if n > 1:
        for i in range(n - 1, -1, -1):
            greater_than_left = i == 0 or numbers[i] > numbers[i - 1]
            greater_than_right = i == n - 1 or numbers[i] > numbers[i + 1]
            if greater_than_left and greater_than_right:
                last_maximum = i + 1
                break
    print('Номер последнего локального максимума:', last_maximum)


# numbers = list(map(float, input('Введите числа через пробел: ').split()))
# solve(numbers)
