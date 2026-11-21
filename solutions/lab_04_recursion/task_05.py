# Задание 5. Бинарный поиск: Напишите функцию, которая рекурсивно выполняет бинарный поиск
# заданного элемента в отсортированном массиве.


def binary_search(numbers, target):

    def search(left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if target < numbers[middle]:
            return search(left, middle - 1)
        return search(middle + 1, right)
    return search(0, len(numbers) - 1)

def solve(numbers, target):
    n = len(numbers)
    ordered = True
    for i in range(1, n):
        if numbers[i] < numbers[i - 1]:
            ordered = False
            break
    if not ordered:
        print('Массив должен быть упорядочен по возрастанию.')
    else:
        index = binary_search(numbers, target)
        if index == -1:
            print('Элемент не найден.')
        else:
            print('Номер найденного элемента:', index + 1)
