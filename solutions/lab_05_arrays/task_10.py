# Задание 10. Дан целочисленный массив размера N, содержащий ровно два одинаковых элемента. Найти
# номера одинаковых элементов и вывести эти номера в порядке возрастания


def solve(numbers):
    n = len(numbers)
    first_number = 0
    second_number = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] == numbers[j]:
                first_number = i + 1
                second_number = j + 1
                break
        if first_number != 0:
            break
    print('Номера одинаковых элементов:', first_number, second_number)
